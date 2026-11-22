#!/usr/bin/env python3
"""SEC-01 before/after invariants on real retained disposable MongoDB databases.

Actual AST source bodies are executed. Only API decorators are removed; the
existing transaction helper is imported unchanged. No .env/server startup,
production data, SMTP, provider, global failpoint or source modification occurs.
"""
import argparse
import ast
import asyncio
import copy
from datetime import datetime, timedelta, timezone
import hashlib
import importlib.metadata
import json
from pathlib import Path
import secrets
import socket
import sys
import time
import uuid
import xml.etree.ElementTree as ET

import bcrypt
from bson import ObjectId
from fastapi import HTTPException, Request
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field, ValidationError
from pymongo.errors import OperationFailure

OUT = Path(__file__).resolve().parent
BACKEND = Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend')
sys.path.insert(0, str(BACKEND))
from mongo_transactions import run_transaction as actual_run_transaction

SELECT = {'now_utc', 'hash_password', 'verify_password', 'ResetPasswordIn', 'reset_password', '_object_id_or_404'}
CASES = []


def require(value, detail):
    if not value:
        raise AssertionError(detail)


def case(identifier, invariant):
    def register(fn):
        CASES.append((identifier, invariant, fn))
        return fn
    return register


async def capture(awaitable):
    try:
        return await awaitable, None
    except Exception as error:
        return None, error


def invalid(error):
    return isinstance(error, HTTPException) and error.status_code == 400 and error.detail == 'Reset link is invalid or expired'


class SessionProxy:
    """Real session lifecycle with one bounded commit-result fault."""
    def __init__(self, real, harness):
        self.real = real
        self.harness = harness

    def __getattr__(self, name):
        return getattr(self.real, name)

    async def __aenter__(self):
        await self.real.__aenter__()
        return self

    async def __aexit__(self, *args):
        return await self.real.__aexit__(*args)

    async def with_transaction(self, callback, **kwargs):
        async def wrapped(_actual_session):
            return await callback(self)
        return await self.real.with_transaction(wrapped, **kwargs)

    async def commit_transaction(self):
        self.harness.commit_calls += 1
        result = await self.real.commit_transaction()
        if self.harness.unknown_commit_once:
            self.harness.unknown_commit_once = False
            raise OperationFailure('Synthetic unknown commit acknowledgement', code=91,
                                   details={'errorLabels': ['UnknownTransactionCommitResult']})
        return result


class ClientProxy:
    def __init__(self, actual, harness):
        self.actual = actual
        self.harness = harness

    async def start_session(self, *args, **kwargs):
        if self.harness.no_transaction:
            raise RuntimeError('Synthetic transaction session unavailable')
        return SessionProxy(await self.actual.start_session(*args, **kwargs), self.harness)


class CollectionProxy:
    def __init__(self, actual, harness, kind):
        self.actual = actual
        self.harness = harness
        self.kind = kind

    def __getattr__(self, name):
        return getattr(self.actual, name)

    @staticmethod
    def kwargs(kwargs):
        result = dict(kwargs)
        if isinstance(result.get('session'), SessionProxy):
            result['session'] = result['session'].real
        return result

    async def find_one(self, *args, **kwargs):
        value = await self.actual.find_one(*args, **self.kwargs(kwargs))
        h = self.harness
        # Only successful token preflight reads are held. Once open, later
        # reads never wait again, so transaction retry cannot deadlock here.
        if self.kind == 'tokens' and value and args and args[0].get('token_hash') == h.target_digest:
            if h.preflight_action and not h.preflight_action_done:
                h.preflight_action_done = True
                if h.preflight_action == 'expire':
                    h.clock = value['expires_at'] + timedelta(seconds=1)
                elif h.preflight_action == 'invalidate':
                    await self.actual.update_one({'_id': value['_id']}, {'$set': {'used': True}})
            if h.barrier_participants:
                h.preflight_reads += 1
                if h.preflight_reads >= h.barrier_participants:
                    h.preflight_open.set()
                await asyncio.wait_for(h.preflight_open.wait(), timeout=30)
        return value

    async def find_one_and_update(self, *args, **kwargs):
        h = self.harness
        if self.kind == 'tokens':
            h.token_write_attempts += 1
            if h.fault == 'token-before' and not h.fault_fired:
                h.fault_fired = True
                raise RuntimeError('Synthetic token write failure')
        return await self.actual.find_one_and_update(*args, **self.kwargs(kwargs))

    async def update_one(self, *args, **kwargs):
        h = self.harness
        if self.kind == 'tokens':
            h.token_write_attempts += 1
            if h.fault == 'token-before' and not h.fault_fired:
                h.fault_fired = True
                raise RuntimeError('Synthetic token write failure')
        if self.kind == 'users':
            h.user_write_attempts += 1
            if h.fault == 'user-before' and not h.fault_fired:
                h.fault_fired = True
                raise RuntimeError('Synthetic user write failure')
        result = await self.actual.update_one(*args, **self.kwargs(kwargs))
        if self.kind == 'users' and h.fault in {'user-after', 'transient-after-user'} and not h.fault_fired:
            h.fault_fired = True
            if h.fault == 'transient-after-user':
                raise OperationFailure('Synthetic transient transaction failure', code=112,
                                       details={'errorLabels': ['TransientTransactionError']})
            raise RuntimeError('Synthetic fault after user write')
        return result


class DBProxy:
    def __init__(self, actual, harness):
        self.actual = actual
        self.users = CollectionProxy(actual.users, harness, 'users')
        self.password_resets = CollectionProxy(actual.password_resets, harness, 'tokens')

    def __getattr__(self, name):
        return self.actual[name]


class Harness:
    def __init__(self, client, db, code, number, run_id):
        self.client = client
        self.actual = db
        self.number = number
        self.run_id = run_id
        self.clock = None
        self.target_digest = None
        self.fault = None
        self.fault_fired = False
        self.unknown_commit_once = False
        self.no_transaction = False
        self.commit_calls = 0
        self.callback_calls = 0
        self.user_write_attempts = 0
        self.token_write_attempts = 0
        self.hash_calls = 0
        self.preflight_action = None
        self.preflight_action_done = False
        self.barrier_participants = 0
        self.preflight_reads = 0
        self.preflight_open = asyncio.Event()

        async def rate_stub(*_args, **_kwargs):
            return None

        async def counted_transaction(tx_client, callback):
            async def counted(session):
                self.callback_calls += 1
                return await callback(session)
            return await actual_run_transaction(tx_client, counted)

        self.ns = {'__name__': 'actual_reset_source_isolation', 'datetime': datetime, 'timezone': timezone,
                   'timedelta': timedelta, 'bcrypt': bcrypt, 'ObjectId': ObjectId,
                   'HTTPException': HTTPException, 'Request': Request, 'BaseModel': BaseModel, 'Field': Field,
                   '_enforce_auth_rate_limit': rate_stub, 'hashlib': hashlib,
                   'run_transaction': counted_transaction, 'client': ClientProxy(client, self)}
        exec(code, self.ns)
        actual_clock = self.ns['now_utc']
        self.ns['now_utc'] = lambda: self.clock or actual_clock()
        actual_hash = self.ns['hash_password']

        def count_hash(value):
            self.hash_calls += 1
            return actual_hash(value)
        self.ns['hash_password'] = count_hash
        self.ns['db'] = DBProxy(db, self)
        self.user = None
        self.initial_hash = None

    async def seed(self):
        # The initial bcrypt operation is not a reset call and is excluded from
        # the per-request hash counter.
        self.initial_hash = self.ns['hash_password']('Initial synthetic fixture password!')
        self.hash_calls = 0
        self.user = {'_id': ObjectId(), 'email': f'fixture-{self.number}-{self.run_id}@example.com',
                     'role': 'customer', 'password_hash': self.initial_hash, 'validation_run': self.run_id}
        await self.actual.users.insert_one(self.user)

    async def token(self, *, used=False, expires=None, user_id=None):
        raw = secrets.token_urlsafe(36)
        digest = hashlib.sha256(raw.encode()).hexdigest()
        record = {'_id': ObjectId(), 'token_hash': digest, 'user_id': str(user_id or self.user['_id']),
                  'created_at': datetime.now(timezone.utc),
                  'expires_at': expires or datetime.now(timezone.utc) + timedelta(minutes=30),
                  'used': used, 'validation_run': self.run_id}
        await self.actual.password_resets.insert_one(record)
        self.target_digest = digest
        return raw, record

    async def reset(self, token, password='Changed synthetic fixture password!'):
        body = self.ns['ResetPasswordIn'](token=token, new_password=password)
        request = Request({'type': 'http', 'method': 'POST', 'path': '/auth/password/reset',
                           'headers': [], 'client': ('127.0.0.1', 12345), 'scheme': 'http',
                           'server': ('127.0.0.1', 0), 'query_string': b''})
        return await self.ns['reset_password'](body, request)

    async def state(self, record):
        return (await self.actual.users.find_one({'_id': self.user['_id']}),
                await self.actual.password_resets.find_one({'_id': record['_id']}))

    async def unchanged_and_unused(self, record):
        user, token = await self.state(record)
        return user['password_hash'] == self.initial_hash and token['used'] is False

    async def accepted(self, record, password='Changed synthetic fixture password!'):
        user, token = await self.state(record)
        return token['used'] is True and self.ns['verify_password'](password, user['password_hash'])


@case('SEC01-01', 'Valid reset preserves the existing response and atomically updates both records')
async def valid(h, o):
    token, record = await h.token()
    result, error = await capture(h.reset(token))
    require(error is None and result == {'reset': True, 'message': 'Password updated. Please sign in again.'}, 'Valid reset response changed or failed')
    require(await h.accepted(record), 'Valid reset did not persist matching password and consumed token')


@case('SEC01-02', 'Unknown token returns existing400 without password hashing or writes')
async def unknown(h, o):
    _, error = await capture(h.reset(secrets.token_urlsafe(36)))
    user = await h.actual.users.find_one({'_id': h.user['_id']})
    require(invalid(error), 'Invalid token did not retain existing400 response')
    require(user['password_hash'] == h.initial_hash and h.hash_calls == 0, 'Invalid token hashed or changed a password')


@case('SEC01-03', 'Expired token is rejected before TTL deletion without writes')
async def expired(h, o):
    token, record = await h.token(expires=datetime.now(timezone.utc) - timedelta(minutes=1))
    _, error = await capture(h.reset(token))
    require(invalid(error) and await h.unchanged_and_unused(record), 'Expired token was accepted or mutated state')
    require(h.hash_calls == 0, 'Expired preflight performed password hashing')


@case('SEC01-04', 'Already consumed token remains rejected')
async def used(h, o):
    token, record = await h.token(used=True)
    _, error = await capture(h.reset(token))
    user, saved = await h.state(record)
    require(invalid(error) and user['password_hash'] == h.initial_hash and saved['used'] is True, 'Used-token handling changed')


@case('SEC01-05', 'Sequential replay cannot overwrite a committed password')
async def replay(h, o):
    token, record = await h.token()
    result, error = await capture(h.reset(token))
    require(error is None, 'Initial valid reset failed')
    _, error = await capture(h.reset(token, 'Different synthetic retry password!'))
    require(invalid(error) and await h.accepted(record), 'Replay accepted or overwrote the first committed password')


@case('SEC01-06', 'Two synchronized valid preflight reads permit exactly one successful reset')
async def concurrency_two(h, o):
    token, record = await h.token()
    h.barrier_participants = 2
    results = await asyncio.gather(*(capture(h.reset(token)) for _ in range(2)))
    accepted = sum(error is None for _, error in results)
    rejected = sum(invalid(error) for _, error in results)
    o.update({'synchronized_preflight_reads': h.preflight_reads, 'accepted': accepted, 'rejected400': rejected})
    require(accepted == 1 and rejected == 1, 'Two same-token consumers did not produce exactly one success and one400')
    require(await h.accepted(record), 'Winning concurrent reset did not persist paired state')


@case('SEC01-07', 'Three rounds of eight synchronized same-token requests have one winner each')
async def concurrency_many(h, o):
    rounds = []
    for _ in range(3):
        token, record = await h.token()
        h.barrier_participants = 8
        h.preflight_reads = 0
        h.preflight_open = asyncio.Event()
        results = await asyncio.gather(*(capture(h.reset(token)) for _ in range(8)))
        accepted = sum(error is None for _, error in results)
        rejected = sum(invalid(error) for _, error in results)
        rounds.append({'accepted': accepted, 'rejected400': rejected})
        require(accepted == 1 and rejected == 7, 'A repeated eight-way concurrency round did not have exactly one winner')
        require(await h.accepted(record), 'Concurrent round left inconsistent paired state')
    o['rounds'] = rounds


async def aborted_state_and_retry(h, o, fault):
    token, record = await h.token()
    h.fault = fault
    _, error = await capture(h.reset(token))
    unchanged = await h.unchanged_and_unused(record)
    o.update({'injected_fault_fired': h.fault_fired, 'error_type': type(error).__name__ if error else None,
              'password_and_token_unchanged_after_abort': unchanged})
    require(h.fault_fired and error is not None, 'Injected failure did not reach the intended operation')
    require(unchanged, 'An aborted reset left a committed password or consumed token')
    result, error = await capture(h.reset(token))
    require(error is None and result.get('reset') is True and await h.accepted(record), 'Clean retry after abort did not succeed exactly once')
    _, error = await capture(h.reset(token, 'Duplicate retry synthetic password!'))
    require(invalid(error) and await h.accepted(record), 'Replay after successful abort recovery changed state')


@case('SEC01-08', 'Token-write failure leaves no partial password change and allows safe retry')
async def token_fault(h, o):
    await aborted_state_and_retry(h, o, 'token-before')


@case('SEC01-09', 'User-write failure after a claim rolls back token consumption')
async def user_before(h, o):
    await aborted_state_and_retry(h, o, 'user-before')


@case('SEC01-10', 'Fault after the real user write but before commit rolls back both documents')
async def user_after(h, o):
    await aborted_state_and_retry(h, o, 'user-after')


@case('SEC01-11', 'Transient transaction failure retries the body with only one durable paired result')
async def transient(h, o):
    token, record = await h.token()
    h.fault = 'transient-after-user'
    result, error = await capture(h.reset(token))
    o.update({'error_type': type(error).__name__ if error else None, 'callback_calls': h.callback_calls,
              'user_write_attempts': h.user_write_attempts, 'password_hash_calls': h.hash_calls})
    require(error is None and result.get('reset') is True, 'Transient failure was not safely retried')
    require(h.callback_calls >= 2 and h.user_write_attempts >= 2, 'Transient test did not rerun the actual callback after abort')
    require(h.hash_calls == 1 and await h.accepted(record), 'Transient retry did not retain one prepared hash and durable paired state')
    _, error = await capture(h.reset(token, 'Replay synthetic transient password!'))
    require(invalid(error) and await h.accepted(record), 'Transient recovery left the token reusable')


@case('SEC01-12', 'Unknown commit acknowledgement retries commit without rerunning password writes')
async def unknown_commit(h, o):
    token, record = await h.token()
    h.unknown_commit_once = True
    result, error = await capture(h.reset(token))
    o.update({'error_type': type(error).__name__ if error else None, 'commit_calls': h.commit_calls,
              'callback_calls': h.callback_calls, 'user_write_attempts': h.user_write_attempts,
              'token_write_attempts': h.token_write_attempts})
    require(error is None and result.get('reset') is True, 'Unknown commit result did not recover safely')
    require(h.commit_calls == 2 and h.callback_calls == 1 and h.user_write_attempts == 1 and h.token_write_attempts == 1,
            'Unknown commit acknowledgement replayed the reset body or failed to retry commit')
    require(await h.accepted(record), 'Unknown commit recovery lost paired durable state')


@case('SEC01-13', 'Lost response after committed success cannot make a retry overwrite the password')
async def lost_response(h, o):
    token, record = await h.token()
    async def invoke_and_lose():
        await h.reset(token)
        raise RuntimeError('Synthetic response lost after completed reset')
    _, error = await capture(invoke_and_lose())
    require(isinstance(error, RuntimeError) and await h.accepted(record), 'Lost-response fixture did not follow durable success')
    _, error = await capture(h.reset(token, 'New response-retry synthetic password!'))
    require(invalid(error) and await h.accepted(record), 'Response-loss retry changed an already committed reset')


@case('SEC01-14', 'Missing target user cannot return success or consume a token')
async def absent_user(h, o):
    token, record = await h.token(user_id=ObjectId())
    _, error = await capture(h.reset(token))
    saved = await h.actual.password_resets.find_one({'_id': record['_id']})
    require(invalid(error) and saved['used'] is False, 'Missing-user reset reported success or committed token consumption')


@case('SEC01-15', 'Expiry is rechecked after successful preflight and before transactional claim')
async def expiry_between(h, o):
    token, record = await h.token()
    h.preflight_action = 'expire'
    _, error = await capture(h.reset(token))
    require(invalid(error) and await h.unchanged_and_unused(record), 'Token expired after preflight was accepted')


@case('SEC01-16', 'A token consumed after preflight is rejected by the fresh claim')
async def invalidated_between(h, o):
    token, record = await h.token()
    h.preflight_action = 'invalidate'
    _, error = await capture(h.reset(token))
    user, saved = await h.state(record)
    require(invalid(error) and user['password_hash'] == h.initial_hash and saved['used'] is True,
            'A token invalidated after preflight still changed the password')


@case('SEC01-17', 'Only the account bound to the token receives the password update')
async def association(h, o):
    other_id = ObjectId()
    await h.actual.users.insert_one({'_id': other_id, 'password_hash': h.initial_hash, 'role': 'customer', 'validation_run': h.run_id})
    token, record = await h.token()
    result, error = await capture(h.reset(token))
    other = await h.actual.users.find_one({'_id': other_id})
    require(error is None and result.get('reset') is True and await h.accepted(record), 'Target account reset failed')
    require(other['password_hash'] == h.initial_hash, 'Token reset modified an unrelated account')


@case('SEC01-18', 'Unavailable transaction sessions fail closed without a standalone write fallback')
async def no_transaction(h, o):
    token, record = await h.token()
    h.no_transaction = True
    _, error = await capture(h.reset(token))
    require(error is not None and await h.unchanged_and_unused(record), 'Missing transaction support fell back to non-atomic writes')


@case('SEC01-19', 'Existing reset request model length requirements are preserved')
async def model_contract(h, o):
    failures = 0
    for token, password in [('x' * 31, 'valid fixture password'), ('x' * 257, 'valid fixture password'), ('x' * 48, 'short')]:
        try:
            h.ns['ResetPasswordIn'](token=token, new_password=password)
        except ValidationError:
            failures += 1
    require(failures == 3, 'Reset request length contract changed')


@case('SEC01-20', 'Existing transaction helper really rolls back an aborted real Mongo write')
async def engine_rollback(h, o):
    async def write_then_abort(session):
        await h.actual.users.update_one({'_id': h.user['_id']}, {'$set': {'validation_marker': 'abort-only'}}, session=session)
        raise RuntimeError('Synthetic independent transaction abort')
    _, error = await capture(actual_run_transaction(h.client, write_then_abort))
    user = await h.actual.users.find_one({'_id': h.user['_id']})
    require(isinstance(error, RuntimeError) and 'validation_marker' not in user, 'Replica-set transaction rollback control failed')


async def main(args):
    source = args.source.resolve()
    raw = source.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    tree = ast.parse(raw.decode(), str(source))
    nodes, refs = [], []
    for node in tree.body:
        chosen = isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node.name in SELECT
        if isinstance(node, ast.Assign):
            chosen = any(isinstance(t, ast.Name) and t.id == 'BCRYPT_ROUNDS' for t in node.targets)
        if chosen:
            cloned = copy.deepcopy(node)
            if isinstance(cloned, (ast.FunctionDef, ast.AsyncFunctionDef)):
                cloned.decorator_list = []
            nodes.append(cloned)
            refs.append({'symbol': getattr(node, 'name', 'BCRYPT_ROUNDS'), 'start': node.lineno, 'end': node.end_lineno,
                         'segment_SHA256': hashlib.sha256(ast.get_source_segment(raw.decode(), node).encode()).hexdigest()})
    require({getattr(x, 'name', 'BCRYPT_ROUNDS') for x in nodes} == SELECT | {'BCRYPT_ROUNDS'}, 'AST symbol set incomplete')
    code = compile(ast.fix_missing_locations(ast.Module(body=nodes, type_ignores=[])), str(source), 'exec', dont_inherit=True)

    run_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '_' + uuid.uuid4().hex[:8]
    db_name = 'comein_sec01_focused_' + args.stage + '_' + run_id.lower()
    started = datetime.now(timezone.utc).isoformat()
    client = AsyncIOMotorClient('mongodb://127.0.0.1:27018/?replicaSet=rs0', serverSelectionTimeoutMS=6000, tz_aware=True)
    hello = await client.admin.command('hello')
    require(hello.get('setName') == 'rs0' and hello.get('isWritablePrimary') is True, 'Expected local replica set PRIMARY unavailable')
    require(all(x.startswith(('127.0.0.1:', 'localhost:')) for x in hello.get('hosts', [])), 'Nonlocal replica-set member rejected')
    db = client[db_name]
    # The fixture DB has no indexes/migrations beyond implicit _id. All data is
    # newly generated synthetic material,retained after the run.
    results = []
    suite = ET.Element('testsuite', name='SEC01 focused ' + args.stage, tests=str(len(CASES)), timestamp=started)
    for number, (identifier, invariant, fn) in enumerate(CASES, 1):
        h = Harness(client, db, code, number, run_id)
        await h.seed()
        began = time.monotonic()
        observation = {}
        status, failure = 'PASS', None
        try:
            await asyncio.wait_for(fn(h, observation), timeout=75)
        except AssertionError as error:
            status, failure = 'FAIL', str(error)
        except Exception as error:
            status, failure = 'ERROR', type(error).__name__
        duration = time.monotonic() - began
        results.append({'id': identifier, 'invariant': invariant, 'status': status, 'seconds': duration,
                        'failure': failure, 'observations': observation})
        test = ET.SubElement(suite, 'testcase', classname='sec01.focused', name=identifier, time=str(duration))
        if status != 'PASS':
            child = ET.SubElement(test, 'failure' if status == 'FAIL' else 'error', message=failure or status)
            child.text = invariant + ': ' + (failure or status)
        print(identifier, status, failure or '', flush=True)
    counts = {name: sum(x['status'] == name for x in results) for name in ('PASS', 'FAIL', 'ERROR')}
    counts['SKIPPED'] = 0
    suite.set('failures', str(counts['FAIL']))
    suite.set('errors', str(counts['ERROR']))
    suite.set('skipped', '0')
    retained = {'users': await db.users.count_documents({}), 'reset_records': await db.password_resets.count_documents({})}
    result = {'project': 'COME-IN', 'scope': 'SEC-01 focused before/after function integration on real local disposable MongoDB',
              'stage': args.stage, 'started_UTC': started, 'finished_UTC': datetime.now(timezone.utc).isoformat(),
              'source': str(source), 'source_SHA256': sha, 'source_SHA256_after': hashlib.sha256(source.read_bytes()).hexdigest(),
              'extracted_symbols': refs, 'transaction_helper': str(BACKEND / 'mongo_transactions.py'),
              'transaction_helper_SHA256': hashlib.sha256((BACKEND / 'mongo_transactions.py').read_bytes()).hexdigest(),
              'runner_SHA256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'python': sys.version, 'executable': sys.executable,
              'versions': {x: importlib.metadata.version(x) for x in ('motor', 'pymongo', 'bcrypt', 'pydantic', 'fastapi')},
              'database': db_name, 'replica_set': 'rs0', 'counts': counts, 'cases': results,
              'retained_records': retained, 'command': [sys.executable, '-B', str(Path(__file__).resolve()), '--stage', args.stage, '--source', str(source)],
              'safety': {'source_modified': False, 'production_access': False, 'provider_calls': 0, 'global_failpoints': 0,
                         'DB_drops': 0, 'raw_tokens_passwords_or_secrets_written': False, 'database_retained': True},
              'limitations': ['Function bodies and model source are actual AST extraction;API decorators alone removed;not full HTTP routing/middleware integration.',
                             'Authentication throttle is an isolated no-op to keep this focused suite from changing or adjudicating SEC-04;old broader suite separately verifies it.',
                             'Collection fault wrappers forward actual Motor sessions and inject deterministic one-shot local errors;no global Mongo failpoint or provider call.',
                             'Commit-acknowledgement and session-unavailable paths are controlled client-boundary faults over the real replica-set session,not actual network outages or a standalone server.']}
    (OUT / ('focused-' + args.stage + '.json')).write_text(json.dumps(result, indent=2) + '\n')
    ET.ElementTree(suite).write(OUT / ('focused-' + args.stage + '.xml'), encoding='utf-8', xml_declaration=True)
    client.close()
    require(result['source_SHA256_after'] == sha, 'Source bytes changed during this run')
    print(json.dumps({'stage': args.stage, 'counts': counts, 'database_retained': db_name}), flush=True)
    return 1 if counts['FAIL'] or counts['ERROR'] else 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--stage', required=True, choices=['before', 'after'])
    parser.add_argument('--source', required=True, type=Path)
    args = parser.parse_args()
    # No .env or external credentials are read. Network addresses are bounded to
    # the already verified loopback replica set by the URI and hello validation.
    raise SystemExit(asyncio.run(main(args)))
