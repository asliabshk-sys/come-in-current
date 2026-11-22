"""Load explicitly selected current/snapshotted server with isolated test env."""
from pathlib import Path
import os,sys,types
import isolated_backend_guard
isolated_backend_guard.install()
assert os.environ['APP_ENV']=='test'
assert os.environ['DB_NAME'].startswith('comein_disposable_test_completion_')
assert os.environ['MONGO_URL']=='mongodb://127.0.0.1:27018/?replicaSet=rs0'
actual=Path('/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115/backend/server.py')
selected=Path(os.environ.get('COMEIN_VALIDATION_SERVER_SOURCE',str(actual))).resolve()
module=types.ModuleType('server');module.__file__=str(actual);sys.modules['server']=module
exec(compile(selected.read_text(),str(selected),'exec',dont_inherit=True),module.__dict__)
import uvicorn
uvicorn.run(module.app,host='127.0.0.1',port=int(os.environ['COMEIN_VALIDATION_PORT']),log_level='warning',access_log=False)
