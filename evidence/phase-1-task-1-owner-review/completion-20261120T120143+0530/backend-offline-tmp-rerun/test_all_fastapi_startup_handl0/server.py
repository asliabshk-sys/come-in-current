
from fastapi import FastAPI
app = FastAPI()
@app.on_event("startup")
async def first():
    await db.alpha.create_index("key", unique=True)
@app.on_event("startup")
async def second():
    await db.beta.create_index([("owner", 1), ("created", -1)])
