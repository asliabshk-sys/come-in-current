#!/usr/bin/env bash
set -euo pipefail
TOOLS=/workspace/come-in-tools
PROJECT=/workspace/come-in-dev/COME-IN-COMPLETE-MASTER-SOURCE-20261115
export YARN_CACHE_FOLDER="$TOOLS/yarn-cache" EXPO_NO_TELEMETRY=1 CI=1
mkdir -p "$TOOLS/mongo-data"
if docker container inspect comein-onboarding-mongo >/dev/null 2>&1; then
  docker start comein-onboarding-mongo >/dev/null
else
  docker run -d --name comein-onboarding-mongo --network host --mount type=bind,src="$TOOLS/mongo-data",dst=/data/db mongo@sha256:8bb4442761a63a8dda452744082cdac9644b429807eb977b42324a63cef59ca4 mongod --replSet rs0 --bind_ip 127.0.0.1 --port 27018 --wiredTigerCacheSizeGB 0.5
fi
for i in $(seq 1 30); do
  docker exec comein-onboarding-mongo mongosh --quiet --port 27018 --eval 'db.adminCommand({ping:1}).ok' >/dev/null 2>&1 && break
  sleep 1
done
docker exec comein-onboarding-mongo mongosh --quiet --port 27018 --eval 'try { rs.status() } catch(e) { if(e.codeName !== "NotYetInitialized") throw e; rs.initiate({_id:"rs0",members:[{_id:0,host:"127.0.0.1:27018"}]}) }' >/dev/null
for i in $(seq 1 30); do
  docker exec comein-onboarding-mongo mongosh --quiet --port 27018 --eval 'if(!db.hello().isWritablePrimary) quit(1)' >/dev/null 2>&1 && break
  sleep 1
done
cd "$PROJECT"
"$TOOLS/py311/bin/python" scripts/mongo/comein_mongo.py init
"$TOOLS/py311/bin/python" scripts/mongo/comein_mongo.py health
if ! curl -fsS http://127.0.0.1:8001/api/ >/dev/null; then
  (cd backend && nohup "$TOOLS/py311/bin/python" -m uvicorn server:app --host 0.0.0.0 --port 8001 > "/workspace/come-in-current/evidence/session-20261117/backend.log" 2>&1 &)
fi
if ! curl -fsS http://127.0.0.1:3000/ >/dev/null; then
  (cd frontend && nohup "$TOOLS/yarn/node_modules/.bin/yarn" web --host lan --port 3000 --max-workers 2 > "/workspace/come-in-current/evidence/session-20261117/frontend.log" 2>&1 &)
fi
for i in $(seq 1 45); do
  if curl -fsS http://127.0.0.1:8001/api/ >/dev/null && curl -fsS http://127.0.0.1:3000/ >/dev/null; then break; fi
  sleep 1
done
curl -fsS http://127.0.0.1:8001/api/
curl -fsS http://127.0.0.1:3000/ -o "/workspace/come-in-current/evidence/session-20261117/frontend-response.html"
