"""Start unmodified FastAPI server with caller's isolated test-only environment."""
import os
import backend_local_guard
backend_local_guard.install()
assert os.environ['APP_ENV']=='test'
assert os.environ['DB_NAME'].startswith('comein_disposable_test_review_')
assert os.environ['MONGO_URL']=='mongodb://127.0.0.1:27018/?replicaSet=rs0'
import server
import uvicorn
uvicorn.run(server.app,host='127.0.0.1',port=int(os.environ['COMEIN_VALIDATION_PORT']),log_level='warning',access_log=False)

