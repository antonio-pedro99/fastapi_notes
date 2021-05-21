from typing import List, Optional

import uvicorn
import database as db
from fastapi import FastAPI
from crud import router

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def startup():
    if not db.database.is_connected:
        await db.database.connect()

@app.on_event("shutdown")
async def shutdwon():
    if db.database.is_connected:
        await db.database.disconnect()


if __name__ == "__main__":
    uvicorn.run("app:app", reload = True)