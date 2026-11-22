"""Create only an isolated SEC-05/09 candidate; production source stays untouched."""
from pathlib import Path
import ast,difflib,hashlib,json

P=Path(__file__).resolve().parent
BASE=P.parent/'before/backend/server.py'
SOURCE=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py')
before=BASE.read_text()
assert hashlib.sha256(before.encode()).hexdigest()=='70f5ee7be1bd94cd96d0fb7dbcb89c067cd7224a05bc1422e069a51538fddd07'
text=before.replace('class StatusCheckCreate(BaseModel):\n    client_name: str\n','class StatusCheckCreate(BaseModel):\n    client_name: str = Field(min_length=1, max_length=256)\n')
text=text.replace('async def create_status_check(payload: StatusCheckCreate):','async def create_status_check(payload: StatusCheckCreate, _: dict = Depends(require_role("admin"))):')
text=text.replace('async def list_status_checks():','async def list_status_checks(_: dict = Depends(require_role("admin"))):')
tree=ast.parse(text)
n=next(n for n in tree.body if isinstance(n,ast.AsyncFunctionDef) and n.name=='admin_update_user_role')
replacement='''async def admin_update_user_role(user_id: str, body: AdminRoleUpdateIn, user: dict = Depends(require_role("admin"))):
    oid = _object_id_or_404(user_id, "User")
    if str(oid) == str(user.get("id")) and body.role != "admin":
        raise HTTPException(status_code=409, detail="You cannot remove your own admin role from this session")
    actor_oid = _object_id_or_404(user["id"], "User")
    guard_id = "admin-role-mutations"
    # Initialize the shared serialization document without migrating user data.
    try:
        await db.security_locks.update_one(
            {"_id": guard_id}, {"$setOnInsert": {"version": 0}}, upsert=True,
        )
    except DuplicateKeyError:
        if not await db.security_locks.find_one({"_id": guard_id}):
            raise

    async def apply(session):
        # Every role mutation writes this same document before reading role/count.
        # Concurrent transactions therefore retry instead of allowing write skew.
        guarded = await db.security_locks.update_one(
            {"_id": guard_id}, {"$inc": {"version": 1}}, session=session,
        )
        if guarded.matched_count != 1:
            raise HTTPException(status_code=503, detail="Role update could not be serialized")
        actor = await db.users.find_one({"_id": actor_oid, "role": "admin"}, session=session)
        if not actor:
            raise HTTPException(status_code=403, detail="Forbidden")
        target = await db.users.find_one({"_id": oid}, session=session)
        if not target:
            raise HTTPException(status_code=404, detail="User not found")
        if target.get("role") == "admin" and body.role != "admin":
            admin_count = await db.users.count_documents({"role": "admin"}, session=session)
            if admin_count <= 1:
                raise HTTPException(status_code=409, detail="The last admin account cannot be demoted")
        changed = await db.users.update_one(
            {"_id": oid},
            {"$set": {"role": body.role, "updated_at": now_utc(), "role_updated_by": user["id"]}},
            session=session,
        )
        if changed.matched_count != 1:
            raise HTTPException(status_code=404, detail="User not found")
        fresh = await db.users.find_one(
            {"_id": oid}, {"password_hash": 0, "password_reset_token_hash": 0}, session=session,
        )
        return doc_out(fresh)

    return await run_transaction(client, apply)'''
lines=text.splitlines(keepends=True)
text=''.join(lines[:n.lineno-1])+replacement+'\n'+''.join(lines[n.end_lineno:])
ast.parse(text)
(P/'server.candidate.py').write_text(text)
(P/'SEC05_SEC09_CANDIDATE.patch').write_text(''.join(difflib.unified_diff(before.splitlines(True),text.splitlines(True),fromfile='before/backend/server.py',tofile='candidate/backend/server.py')))
tb=ast.parse(before);ta=ast.parse(text)
changed=[]
for b,a in zip(tb.body,ta.body):
    if ast.dump(b,include_attributes=False)!=ast.dump(a,include_attributes=False):changed.append(getattr(a,'name',type(a).__name__))
assert changed==['StatusCheckCreate','create_status_check','list_status_checks','admin_update_user_role'],changed
meta={'source_base_SHA256':hashlib.sha256(before.encode()).hexdigest(),'candidate_SHA256':hashlib.sha256(text.encode()).hexdigest(),
      'changed_AST_nodes':changed,'imports_changed':False,'production_source_modified':False,
      'schema_delta':'Dedicated security_locks control document with _id/admin-role-mutations and version integer;implicit _id index only,no migration/user deletion.',
      'SEC01_reset_password_unchanged':ast.dump(next(n for n in tb.body if isinstance(n,ast.AsyncFunctionDef) and n.name=='reset_password'),include_attributes=False)==ast.dump(next(n for n in ta.body if isinstance(n,ast.AsyncFunctionDef) and n.name=='reset_password'),include_attributes=False)}
(P/'candidate-metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta))
