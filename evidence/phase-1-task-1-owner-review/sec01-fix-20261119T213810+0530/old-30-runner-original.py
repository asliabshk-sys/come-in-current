#!/usr/bin/env python3
"""Isolated source-bound security validation; no application import or source edits.

Only a newly named localhost MongoDB database receives synthetic fixtures. Actual
server functions/classes are compiled from their original AST nodes; API route
decorators alone are removed. SMTP is replaced at its transport boundary. This
is function-level local integration, not deployed HTTP/provider verification.
"""
from __future__ import annotations

import ast
import asyncio
import copy
import hashlib
import importlib.metadata
import json
import logging
from pathlib import Path
import re
import secrets
import smtplib
import socket
import sys
import time
import types
from datetime import datetime, timedelta, timezone
from typing import Optional
import uuid
import xml.etree.ElementTree as ET

import bcrypt
from bson import ObjectId
from fastapi import Depends, HTTPException, Request
import jwt
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, EmailStr, Field, ValidationError

OUT = Path(__file__).resolve().parent
SOURCE = Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py')
PREVIOUS = OUT.parent / 'iteration-2026-11-18T072632-0800'
RUN_ID = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '_' + uuid.uuid4().hex[:10]
DB_NAME = 'comein_reset_validation_' + RUN_ID.lower()
URI = 'mongodb://127.0.0.1:27018/?replicaSet=rs0'
FUNCTIONS = [
    'now_utc', 'doc_out', 'hash_password', 'verify_password', '_jwt_secret',
    'create_access_token', 'get_bearer_token', 'get_current_user_optional',
    'get_current_user', 'require_role', '_client_ip', '_rate_keys',
    '_check_auth_rate_limit', '_record_auth_attempt', '_enforce_auth_rate_limit',
    'ForgotPasswordIn', 'ResetPasswordIn', '_send_password_reset_email',
    'forgot_password', 'reset_password', '_object_id_or_404',
]
CONSTANTS = ['BCRYPT_ROUNDS', 'JWT_ALG', 'ACCESS_TTL_MIN', 'AUTH_RATE_LIMITS', 'AUTH_IP_MULTIPLIER']
RAW = SOURCE.read_bytes()
TREE = ast.parse(RAW.decode(), str(SOURCE))
SELECTED = []
SOURCE_REFS = []
for node in TREE.body:
    picked = isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node.name in FUNCTIONS
    if isinstance(node, ast.Assign):
        picked = any(isinstance(t, ast.Name) and t.id in CONSTANTS for t in node.targets)
    if picked:
        SOURCE_REFS.append({'symbol': getattr(node, 'name', ast.unparse(node.targets[0]) if isinstance(node, ast.Assign) else ''),
                            'start': node.lineno, 'end': node.end_lineno,
                            'sha256_original_source_segment': hashlib.sha256(ast.get_source_segment(RAW.decode(), node).encode()).hexdigest()})
        copied = copy.deepcopy(node)
        if isinstance(copied, (ast.FunctionDef, ast.AsyncFunctionDef)):
            copied.decorator_list = []
        SELECTED.append(copied)
MODULE = ast.Module(body=SELECTED, type_ignores=[])
# server.py has no future-annotations import: prevent this harness's own flag
# from altering the actual model annotation evaluation semantics.
CODE = compile(ast.fix_missing_locations(MODULE), str(SOURCE), 'exec', dont_inherit=True)


class InvariantFailure(AssertionError):
    pass


def require(condition, message):
    if not condition:
        raise InvariantFailure(message)


class LogCapture(logging.Handler):
    def __init__(self):
        super().__init__()
        self.messages = []

    def emit(self, record):
        self.messages.append(record.getMessage())


SMTP_MESSAGES = []
SMTP_MODE = 'ok'


class OfflineSMTP:
    """Real email-helper content construction, zero email/network transmission."""
    def __init__(self, host, port, timeout):
        require(host == 'smtp.invalid', 'SMTP attempted to use unexpected host')
        self.started = False

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def starttls(self):
        if SMTP_MODE == 'tls_failure':
            raise RuntimeError('synthetic transport failure')
        self.started = True

    def login(self, *args):
        require(self.started, 'SMTP authentication must follow STARTTLS')

    def send_message(self, msg):
        require(self.started, 'SMTP send must follow STARTTLS')
        SMTP_MESSAGES.append(msg)


class DBProxy:
    def __init__(self, actual, **overrides):
        self.actual = actual
        self.overrides = overrides

    def __getattr__(self, name):
        return self.overrides.get(name, self.actual[name])


class ReadBarrier:
    """Both real database reads complete before either function can continue."""
    def __init__(self, collection, method='find_one'):
        self.actual = collection
        self.method = method
        self.arrivals = 0
        self.open = asyncio.Event()

    def __getattr__(self, name):
        if name != self.method:
            return getattr(self.actual, name)

        async def operation(*args, **kwargs):
            value = await getattr(self.actual, name)(*args, **kwargs)
            self.arrivals += 1
            if self.arrivals >= 2:
                self.open.set()
            await asyncio.wait_for(self.open.wait(), 8)
            return value
        return operation


class FaultAfterPasswordWrite:
    def __init__(self, collection):
        self.actual = collection

    def __getattr__(self, name):
        return getattr(self.actual, name)

    async def update_one(self, *args, **kwargs):
        raise RuntimeError('synthetic token-mark write failure')


class Harness:
    def __init__(self, db, number):
        self.db = db
        self.number = number
        self.email = f'reset-fixture-{number}-{RUN_ID.lower()}@example.com'
        self.ip = f'127.0.0.{number}'
        self.logs = LogCapture()
        self.logger = logging.Logger(f'isolated-reset-{number}')
        self.logger.addHandler(self.logs)
        self.env = {'JWT_SECRET': secrets.token_urlsafe(48), 'SMTP_HOST': 'smtp.invalid',
                    'SMTP_FROM': 'noreply@example.com', 'PASSWORD_RESET_URL': 'https://reset.invalid/password-reset',
                    'SMTP_PORT': '587'}
        self.ns = {'__name__': 'isolated_actual_server_functions', 'datetime': datetime, 'timezone': timezone,
                   'timedelta': timedelta, 'Optional': Optional, 'bcrypt': bcrypt, 'jwt': jwt, 'ObjectId': ObjectId,
                   'HTTPException': HTTPException, 'Request': Request, 'Depends': Depends, 'BaseModel': BaseModel,
                   'EmailStr': EmailStr, 'Field': Field, 'os': types.SimpleNamespace(environ=self.env),
                   'secrets': secrets, 'hashlib': hashlib, 'logger': self.logger, 'db': db}
        exec(CODE, self.ns)
        self.user = None
        self.initial_hash = None

    def request(self, *, token=None, forwarded=None):
        headers = []
        if token is not None:
            headers.append((b'authorization', ('Bearer ' + token).encode()))
        if forwarded is not None:
            headers.append((b'x-forwarded-for', forwarded.encode()))
        return Request({'type': 'http', 'method': 'POST', 'path': '/isolated-validation',
                        'headers': headers, 'client': (self.ip, 12345), 'scheme': 'http',
                        'server': ('127.0.0.1', 0), 'query_string': b''})

    async def seed_user(self):
        self.initial_hash = self.ns['hash_password']('Initial fixture password!')
        self.user = {'_id': ObjectId(), 'email': self.email, 'name': 'Synthetic reset fixture',
                     'role': 'customer', 'password_hash': self.initial_hash, 'validation_run': RUN_ID}
        await self.db.users.insert_one(self.user)
        return self.user

    async def seed_token(self, *, expires=None, used=False, user_id=None):
        token = secrets.token_urlsafe(36)
        record = {'_id': ObjectId(), 'user_id': str(user_id or self.user['_id']),
                  'token_hash': hashlib.sha256(token.encode()).hexdigest(),
                  'created_at': self.ns['now_utc'](),
                  'expires_at': expires or self.ns['now_utc']() + timedelta(minutes=30),
                  'used': used, 'validation_run': RUN_ID}
        await self.db.password_resets.insert_one(record)
        return token, record

    async def forgot(self, email=None):
        return await self.ns['forgot_password'](self.ns['ForgotPasswordIn'](email=email or self.email), self.request())

    async def reset(self, token, password='Changed fixture password!'):
        return await self.ns['reset_password'](self.ns['ResetPasswordIn'](token=token, new_password=password), self.request())

    async def user_now(self):
        return await self.db.users.find_one({'_id': self.user['_id']})


CASES = []


def case(name, invariant, scope='local MongoDB function integration'):
    def register(fn):
        CASES.append((name, invariant, scope, fn))
        return fn
    return register


@case('RESET-01', 'Forgot input rejects invalid email', 'actual Pydantic model unit')
async def invalid_email(h, o):
    try:
        h.ns['ForgotPasswordIn'](email='invalid-email')
    except ValidationError:
        return
    require(False, 'Invalid email was accepted')


@case('RESET-02', 'Reset input rejects a token shorter than 32 characters', 'actual Pydantic model unit')
async def short_token(h, o):
    try:
        h.ns['ResetPasswordIn'](token='x' * 31, new_password='valid fixture password')
    except ValidationError:
        return
    require(False, 'Short reset token was accepted')


@case('RESET-03', 'Reset input rejects a password shorter than eight characters', 'actual Pydantic model unit')
async def short_password(h, o):
    try:
        h.ns['ResetPasswordIn'](token='x' * 48, new_password='short')
    except ValidationError:
        return
    require(False, 'Short reset password was accepted')


@case('RESET-04', 'Reset input rejects token/password values above declared maxima', 'actual Pydantic model unit')
async def long_values(h, o):
    rejected = 0
    for token, password in [('x' * 257, 'valid fixture password'), ('x' * 48, 'p' * 129)]:
        try:
            h.ns['ResetPasswordIn'](token=token, new_password=password)
        except ValidationError:
            rejected += 1
    require(rejected == 2, 'Declared maximum input lengths were not enforced')


@case('RESET-05', 'Known and unknown forgot calls share a generic response and reveal no raw token')
async def generic_forgot(h, o):
    await h.seed_user()
    known = await h.forgot()
    unknown = await h.forgot(email='unknown-' + h.email)
    require(known == unknown and set(known) == {'message'}, 'Forgot response enumerates account or token')
    require(len(SMTP_MESSAGES) == 1, 'Unknown email caused a reset message')
    body = SMTP_MESSAGES[0].get_content()
    token = re.search(r'\?token=([^\s]+)', body).group(1)
    require(token not in json.dumps(known) and all(token not in x for x in h.logs.messages), 'Raw token leaked to public response/log')


@case('RESET-06', 'Forgot generates a random token, stores SHA256 only, and applies 30-minute expiry')
async def issuance(h, o):
    await h.seed_user()
    before = h.ns['now_utc']()
    await h.forgot()
    after = h.ns['now_utc']()
    token = re.search(r'\?token=([^\s]+)', SMTP_MESSAGES[0].get_content()).group(1)
    stored = await h.db.password_resets.find_one({'user_id': str(h.user['_id'])})
    require(len(token) >= 48 and stored['token_hash'] == hashlib.sha256(token.encode()).hexdigest(), 'Generated token/digest invariant failed')
    require(token not in repr(stored) and not stored['used'], 'Raw token stored or issued token marked used')
    require(before + timedelta(minutes=30) <= stored['expires_at'] <= after + timedelta(minutes=30), 'Issued expiry differs from 30 minutes')
    o.update(stored_digest_only=True, expires_in_minutes=30, actual_smtp_delivery=False)


@case('RESET-07', 'Sequential forgot issuance invalidates an older token')
async def invalidates_previous(h, o):
    await h.seed_user()
    _, previous = await h.seed_token()
    await h.forgot()
    require(await h.db.password_resets.find_one({'_id': previous['_id']}) is None, 'Previous token remained after sequential reissue')
    require(await h.db.password_resets.count_documents({'user_id': str(h.user['_id'])}) == 1, 'Sequential issuance did not leave one token')


@case('RESET-08', 'Missing SMTP configuration leaves no newly usable reset token')
async def missing_smtp(h, o):
    await h.seed_user()
    h.env.pop('SMTP_HOST')
    response = await h.forgot()
    require(set(response) == {'message'}, 'Missing SMTP returned a nongeneric response')
    require(await h.db.password_resets.count_documents({'user_id': str(h.user['_id'])}) == 0, 'Undelivered token remains active')


@case('RESET-09', 'SMTP failure is cleaned up and logs no raw reset token or email')
async def smtp_failure(h, o):
    global SMTP_MODE
    await h.seed_user()
    SMTP_MODE = 'tls_failure'
    await h.forgot()
    require(await h.db.password_resets.count_documents({'user_id': str(h.user['_id'])}) == 0, 'SMTP failure left a usable token')
    require(h.email not in ' '.join(h.logs.messages), 'SMTP failure leaked recipient in application log')
    require(any('RuntimeError' in m for m in h.logs.messages), 'SMTP failure type was not recorded')
    o.update(application_log_messages=len(h.logs.messages), actual_smtp_delivery=False)


@case('RESET-10', 'Invalid SMTP port fails safely with generic response and token cleanup')
async def invalid_smtp_port(h, o):
    await h.seed_user()
    h.env['SMTP_PORT'] = 'not-a-port'
    escaped = False
    try:
        await h.forgot()
    except ValueError:
        escaped = True
    active = await h.db.password_resets.count_documents({'user_id': str(h.user['_id']), 'used': False})
    o.update(configuration_exception_escaped=escaped, active_undelivered_tokens=active)
    require(not escaped and active == 0, 'Invalid SMTP_PORT escapes the handler and leaves an active undelivered token')


@case('RESET-11', 'A valid token updates password and is consumed')
async def normal_reset(h, o):
    await h.seed_user()
    token, record = await h.seed_token()
    response = await h.reset(token)
    current = await h.user_now()
    stored = await h.db.password_resets.find_one({'_id': record['_id']})
    require(response.get('reset') is True and stored['used'] is True, 'Normal reset did not consume token')
    require(h.ns['verify_password']('Changed fixture password!', current['password_hash']), 'New password was not persisted')
    require(not h.ns['verify_password']('Initial fixture password!', current['password_hash']), 'Old password still matches after reset')
    require('password_hash' not in response and token not in repr(response), 'Sensitive value returned by reset')


async def rejected_without_change(h, token):
    try:
        await h.reset(token)
    except HTTPException as exc:
        require(exc.status_code == 400, 'Invalid token received an unexpected status')
    else:
        require(False, 'Invalid token was accepted')
    require((await h.user_now())['password_hash'] == h.initial_hash, 'Rejected reset changed password')


@case('RESET-12', 'Expired tokens are rejected even before TTL deletion')
async def expired_token(h, o):
    await h.seed_user()
    token, _ = await h.seed_token(expires=h.ns['now_utc']() - timedelta(seconds=1))
    await rejected_without_change(h, token)


@case('RESET-13', 'An invalid random token cannot change password')
async def wrong_token(h, o):
    await h.seed_user()
    await h.seed_token()
    await rejected_without_change(h, secrets.token_urlsafe(36))


@case('RESET-14', 'An already used token cannot change password')
async def used_token(h, o):
    await h.seed_user()
    token, _ = await h.seed_token(used=True)
    await rejected_without_change(h, token)


@case('RESET-15', 'Sequential replay is rejected and does not overwrite the first reset')
async def replay(h, o):
    await h.seed_user()
    token, _ = await h.seed_token()
    await h.reset(token)
    first = (await h.user_now())['password_hash']
    try:
        await h.reset(token, password='Second competing fixture password!')
    except HTTPException as exc:
        require(exc.status_code == 400, 'Replay received an unexpected status')
    else:
        require(False, 'Sequential replay was accepted')
    require((await h.user_now())['password_hash'] == first, 'Replay overwrote password')


@case('RESET-16', 'At most one concurrent request can consume the same reset token')
async def concurrent_reset(h, o):
    await h.seed_user()
    token, record = await h.seed_token()
    barrier = ReadBarrier(h.db.password_resets)
    h.ns['db'] = DBProxy(h.db, password_resets=barrier)
    responses = await asyncio.gather(h.reset(token, 'First concurrent fixture password!'),
                                     h.reset(token, 'Second concurrent fixture password!'), return_exceptions=True)
    accepted = sum(isinstance(r, dict) and r.get('reset') is True for r in responses)
    stored = await h.db.password_resets.find_one({'_id': record['_id']})
    o.update(accepted_resets=accepted, matching_valid_reads=barrier.arrivals, token_used_afterwards=stored['used'],
             controlled_interleaving='Both actual MongoDB token reads finish before either function resumes')
    require(accepted <= 1, 'Two concurrent requests both accepted the same single-use token')


@case('RESET-17', 'A failure between password write and token write leaves no partial state or reusable token')
async def failure_between_writes(h, o):
    await h.seed_user()
    token, record = await h.seed_token()
    h.ns['db'] = DBProxy(h.db, password_resets=FaultAfterPasswordWrite(h.db.password_resets))
    escaped = False
    try:
        await h.reset(token)
    except RuntimeError:
        escaped = True
    after_fault = await h.user_now()
    stored = await h.db.password_resets.find_one({'_id': record['_id']})
    changed = after_fault['password_hash'] != h.initial_hash
    h.ns['db'] = h.db
    retried = await h.reset(token, 'Retry fixture password!')
    o.update(injected_exception_escaped=escaped, password_changed_before_failure=changed,
             token_unused_after_failure=not stored['used'], same_token_retry_accepted=retried.get('reset') is True,
             fault_scope='Token-mark update raises before execution; preceding real users.update_one committed')
    require(not changed or stored['used'], 'Password changed but token stayed unused; same token retry accepted')


@case('RESET-18', 'Reset cannot report success for a missing target account')
async def missing_user(h, o):
    await h.seed_user()
    token, record = await h.seed_token(user_id=ObjectId())
    response = await h.reset(token)
    stored = await h.db.password_resets.find_one({'_id': record['_id']})
    o.update(success_reported=response.get('reset') is True, token_consumed=stored['used'])
    require(response.get('reset') is not True, 'Reset reports success when users.update_one matches zero accounts')


@case('RESET-19', 'Password reset invalidates a previously issued access JWT')
async def old_session(h, o):
    await h.seed_user()
    old_jwt = h.ns['create_access_token'](str(h.user['_id']), 'customer', h.email)
    require(await h.ns['get_current_user_optional'](h.request(token=old_jwt)) is not None, 'Fixture JWT invalid before reset')
    token, _ = await h.seed_token()
    await h.reset(token)
    authenticated = await h.ns['get_current_user_optional'](h.request(token=old_jwt))
    o.update(pre_reset_jwt_still_accepted=authenticated is not None, policy='Security recovery revocation requirement; existing seven-day JWT design does not implement it')
    require(authenticated is None, 'A pre-reset access JWT remains authenticated after password reset')


@case('RESET-20', 'Invalid-signature access JWT is rejected')
async def invalid_jwt(h, o):
    await h.seed_user()
    token = jwt.encode({'sub': str(h.user['_id']), 'type': 'access', 'exp': datetime.now(timezone.utc) + timedelta(minutes=5)}, secrets.token_urlsafe(48), algorithm='HS256')
    require(await h.ns['get_current_user_optional'](h.request(token=token)) is None, 'Invalid JWT signature accepted')


@case('RESET-21', 'Expired access JWT is rejected')
async def expired_jwt(h, o):
    await h.seed_user()
    token = jwt.encode({'sub': str(h.user['_id']), 'type': 'access', 'exp': datetime.now(timezone.utc) - timedelta(minutes=5)}, h.env['JWT_SECRET'], algorithm='HS256')
    require(await h.ns['get_current_user_optional'](h.request(token=token)) is None, 'Expired JWT accepted')


@case('RESET-22', 'Non-access JWT type is rejected')
async def wrong_jwt_type(h, o):
    await h.seed_user()
    token = jwt.encode({'sub': str(h.user['_id']), 'type': 'refresh', 'exp': datetime.now(timezone.utc) + timedelta(minutes=5)}, h.env['JWT_SECRET'], algorithm='HS256')
    require(await h.ns['get_current_user_optional'](h.request(token=token)) is None, 'Non-access JWT accepted')


@case('RESET-23', 'JWT for a missing account is rejected')
async def missing_jwt_user(h, o):
    token = h.ns['create_access_token'](str(ObjectId()), 'customer', h.email)
    require(await h.ns['get_current_user_optional'](h.request(token=token)) is None, 'JWT for missing account accepted')


@case('RESET-24', 'Authorization uses current persisted role and strips password hash')
async def role_refresh(h, o):
    await h.seed_user()
    token = h.ns['create_access_token'](str(h.user['_id']), 'admin', h.email)
    result = await h.ns['get_current_user_optional'](h.request(token=token))
    require(result.get('role') == 'customer' and 'password_hash' not in result, 'JWT role overrides database or password hash leaks')
    try:
        await h.ns['require_role']('admin')(user=result)
    except HTTPException as exc:
        require(exc.status_code == 403, 'Wrong role received unexpected status')
    else:
        require(False, 'Non-admin current database role passed admin dependency')


@case('RESET-25', 'Forgot subject limit accepts five attempts then rejects the sixth')
async def rate_serial(h, o):
    for _ in range(5):
        await h.forgot()
    try:
        await h.forgot()
    except HTTPException as exc:
        require(exc.status_code == 429, 'Subject throttle received unexpected status')
    else:
        require(False, 'Sixth forgot subject attempt was accepted')
    keys = h.ns['_rate_keys']('forgot', h.request(), h.email)
    rows = [await h.db.auth_rate_limits.find_one({'_id': key}) for key, _ in keys]
    require(all(r['count'] == 5 for r in rows), 'Rejected attempt unexpectedly incremented counters')
    require(all('expires_at' in r and h.email not in r['_id'] for r in rows), 'Rate keys expose raw email or lack TTL field')
    o.update(allowed=5, rejected=1, counter_keys_hashed=True)


@case('RESET-26', 'Reset IP limit accepts 50 attempts then rejects the next')
async def reset_ip_limit(h, o):
    key, _ = h.ns['_rate_keys']('reset', h.request(), '')[0]
    await h.db.auth_rate_limits.insert_one({'_id': key, 'count': 49, 'expires_at': datetime.now(timezone.utc) + timedelta(minutes=15)})
    await h.ns['_enforce_auth_rate_limit']('reset', h.request())
    try:
        await h.ns['_enforce_auth_rate_limit']('reset', h.request())
    except HTTPException as exc:
        require(exc.status_code == 429, 'IP throttle received unexpected status')
    else:
        require(False, 'Over-limit reset IP attempt was accepted')
    o.update(preseeded_attempts=49, newly_allowed=1, rejected=1)


@case('RESET-27', 'Concurrent rate-limit checks cannot overshoot the configured subject limit')
async def concurrent_rate(h, o):
    for key, factor in h.ns['_rate_keys']('forgot', h.request(), h.email):
        await h.db.auth_rate_limits.insert_one({'_id': key, 'count': 4 if factor == 1 else 0,
                                               'expires_at': datetime.now(timezone.utc) + timedelta(hours=1)})

    class SubjectBarrier(ReadBarrier):
        async def find_one(self, query, *args, **kwargs):
            value = await self.actual.find_one(query, *args, **kwargs)
            if ':sub:' in query['_id']:
                self.arrivals += 1
                if self.arrivals == 2:
                    self.open.set()
                await asyncio.wait_for(self.open.wait(), 8)
            return value

    barrier = SubjectBarrier(h.db.auth_rate_limits)
    h.ns['db'] = DBProxy(h.db, auth_rate_limits=barrier)
    responses = await asyncio.gather(h.ns['_enforce_auth_rate_limit']('forgot', h.request(), h.email),
                                     h.ns['_enforce_auth_rate_limit']('forgot', h.request(), h.email), return_exceptions=True)
    allowed = sum(r is None for r in responses)
    subject_key = h.ns['_rate_keys']('forgot', h.request(), h.email)[1][0]
    stored = await h.db.auth_rate_limits.find_one({'_id': subject_key})
    o.update(initial_subject_count=4, concurrent_allowed=allowed, final_subject_count=stored['count'], configured_subject_limit=5)
    require(allowed <= 1 and stored['count'] <= 5, 'Concurrent check-then-increment exceeded the configured subject cap')


@case('RESET-28', 'Concurrent forgot issuance is measured without inventing an owner token-count policy')
async def concurrent_forgot(h, o):
    await h.seed_user()
    barrier = ReadBarrier(h.db.password_resets, 'delete_many')
    h.ns['db'] = DBProxy(h.db, password_resets=barrier)
    responses = await asyncio.gather(h.forgot(), h.forgot())
    active = await h.db.password_resets.count_documents({'user_id': str(h.user['_id']), 'used': False})
    o.update(active_tokens_after_two_successful_forgot_calls=active, pending_policy='Owner must define one-active-token versus multiple delivered-token acceptance',
             observation_only=True)
    require(len(responses) == 2 and len(SMTP_MESSAGES) == 2, 'Concurrent forgot did not complete both synthetic deliveries')


@case('RESET-29', 'Direct forwarded-IP behavior is measured; trusted-ingress policy remains external')
async def forwarded_ip(h, o):
    value = h.ns['_client_ip'](h.request(forwarded='198.51.100.10, 127.0.0.1'))
    o.update(first_forwarded_value_selected=value == '198.51.100.10',
             production_exploit_or_ingress_validation=False,
             observation_only=True)
    require(value == '198.51.100.10', 'Source helper behavior unexpectedly differs from inspected implementation')


@case('RESET-30', 'Distinct accepted long passwords must not authenticate interchangeably', 'actual model plus bcrypt unit')
async def bcrypt_length(h, o):
    prefix = 'a' * 72
    first = prefix + 'first-suffix'
    second = prefix + 'second-suffix'
    h.ns['ResetPasswordIn'](token='x' * 48, new_password=first)
    h.ns['ResetPasswordIn'](token='x' * 48, new_password=second)
    hashed = h.ns['hash_password'](first)
    aliases = h.ns['verify_password'](second, hashed)
    o.update(model_accepted_both=True, utf8_bytes_exceed_72=True, distinct_suffix_authenticates=aliases)
    require(not aliases, 'Passwords accepted above bcrypt 72-byte boundary authenticate interchangeably')


async def main():
    # Loopback-only firewall for this process, including the Motor worker pool.
    original_connect = socket.socket.connect
    original_create_connection = socket.create_connection
    original_smtp = smtplib.SMTP
    def safe_connect(sock, address):
        if isinstance(address, tuple):
            require(str(address[0]) in {'127.0.0.1', 'localhost', '::1'}, 'Non-loopback connection blocked')
        return original_connect(sock, address)
    socket.socket.connect = safe_connect
    smtplib.SMTP = OfflineSMTP
    client = AsyncIOMotorClient(URI, serverSelectionTimeoutMS=5000, tz_aware=True)
    db = client[DB_NAME]
    started = datetime.now(timezone.utc)
    results = []
    inputs = []
    for name in ['FINAL_EVIDENCE_GAP_CLOSURE_REPORT.md', 'FINAL_SECURITY_VALIDATION_REPORT.md',
                 'FINAL_NAVIGATION_AND_API_INVENTORY.md', 'FINAL_PRESERVATION_VERIFICATION.md',
                 'FINAL_OWNER_DECISION_READINESS.md', 'FINAL_REVIEW_MANIFEST.json',
                 'ITERATION_CHECKPOINT.md', 'reset-flow-validation.json']:
        value = (PREVIOUS / name).read_bytes()
        inputs.append({'path': str(PREVIOUS / name), 'bytes_read': len(value), 'sha256': hashlib.sha256(value).hexdigest()})
    try:
        hello = await client.admin.command('hello')
        require(hello.get('isWritablePrimary') and hello.get('setName') == 'rs0', 'Disposable MongoDB replica set unavailable')
        mongo_version = (await client.admin.command('buildInfo'))['version']
        for number, (case_id, invariant, scope, fn) in enumerate(CASES, 1):
            global SMTP_MODE
            SMTP_MESSAGES.clear()
            SMTP_MODE = 'ok'
            h = Harness(db, number)
            observation = {}
            before = time.monotonic()
            try:
                await asyncio.wait_for(fn(h, observation), timeout=35)
                status, error = 'PASS', None
            except InvariantFailure as exc:
                status, error = 'FAIL', str(exc)
            except Exception as exc:
                # Deliberately omit exception values/locals, which could contain fixtures.
                status, error = 'ERROR', type(exc).__name__
            elapsed = round(time.monotonic() - before, 6)
            results.append({'id': case_id, 'invariant': invariant, 'scope': scope,
                            'status': status, 'duration_seconds': elapsed,
                            'failure': error, 'observations': observation})
            print(f'{case_id} {status} {invariant}', flush=True)
        counts = {k: sum(r['status'] == k for r in results) for k in ['PASS', 'FAIL', 'ERROR', 'SKIPPED']}
        retained_counts = {name: await db[name].count_documents({}) for name in await db.list_collection_names()}
        evidence = {'project': 'COME-IN', 'started_utc': started.isoformat(),
                    'finished_utc': datetime.now(timezone.utc).isoformat(), 'run_id': RUN_ID,
                    'source_path': str(SOURCE), 'source_sha256': hashlib.sha256(RAW).hexdigest(),
                    'source_sha256_after': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                    'extracted_symbols': SOURCE_REFS, 'input_documents_read': inputs,
                    'python': sys.version, 'python_executable': sys.executable,
                    'versions': {name: importlib.metadata.version(name) for name in ['motor', 'pymongo', 'bcrypt', 'PyJWT', 'pydantic', 'fastapi']},
                    'database': {'host': '127.0.0.1', 'port': 27018, 'name': DB_NAME, 'setName': hello['setName'],
                                 'primary': hello['isWritablePrimary'], 'version': mongo_version,
                                 'retained': True, 'collection_document_counts': retained_counts,
                                 'existing_database_used': False, 'drops_or_resets': 0},
                    'test_count': len(results), 'counts': counts, 'cases': results,
                    'safety': {'source_or_configuration_changes': 0, 'application_server_imports': 0,
                               'real_emails': 0, 'provider_calls': 0, 'production_connections': 0,
                               'network_guard': 'socket.connect permits loopback hosts only',
                               'smtp': 'Actual helper executes with OfflineSMTP transport; no messages logged to artifacts',
                               'fixture_secrets': 'Generated only in memory; raw tokens/passwords/JWT secrets omitted from evidence'},
                    'limitations': ['Actual AST-extracted function/model execution with real bcrypt/PyJWT/Pydantic/Motor; not HTTP server/middleware/router execution.',
                                    'Controlled scheduling barriers/fault proxy preserve actual function bodies and real database calls but deliberately force possible interleavings.',
                                    'Synthetic fixtures and local replica set do not prove deployed-user impact, SMTP delivery, production ingress or external provider behavior.',
                                    'Concurrent-forgot and forwarded-IP cases are observation checks, not owner policy/security acceptance.',
                                    'Old-JWT case validates the explicit recovery-revocation security invariant; eventual product policy requires owner decision.']}
        (OUT / 'password-reset-results-v2.json').write_text(json.dumps(evidence, indent=2) + '\n')
        root = ET.Element('testsuites')
        suite = ET.SubElement(root, 'testsuite', name='actual_password_reset_security_local_integration', tests=str(len(results)),
                              failures=str(counts['FAIL']), errors=str(counts['ERROR']), skipped='0', timestamp=started.isoformat())
        for result in results:
            item = ET.SubElement(suite, 'testcase', classname='isolated_actual_server_reset', name=result['id'] + ' ' + result['invariant'], time=str(result['duration_seconds']))
            if result['status'] in {'FAIL', 'ERROR'}:
                ET.SubElement(item, 'failure' if result['status'] == 'FAIL' else 'error', message=result['failure'])
        ET.indent(root)
        ET.ElementTree(root).write(OUT / 'password-reset-junit-v2.xml', encoding='utf-8', xml_declaration=True)
        print(json.dumps({'counts': counts, 'tests': len(results), 'database_retained': DB_NAME, 'source_unchanged': evidence['source_sha256'] == evidence['source_sha256_after']}), flush=True)
        return 1 if counts['FAIL'] or counts['ERROR'] else 0
    finally:
        client.close()
        socket.socket.connect = original_connect
        socket.create_connection = original_create_connection
        smtplib.SMTP = original_smtp


if __name__ == '__main__':
    raise SystemExit(asyncio.run(main()))
