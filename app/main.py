from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api.dependencies import db_manager
from api.routers import (
    account_router, 
    users_router,
    user_groups_router,
    units_router,
    rooms_router,
    room_groups_router,
    events_router,
    invites_router,
    registrations_router,
    permissions_router,
    organization_router,
    buildings_router
    )



@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_manager.db_init()
    yield



app = FastAPI(
    title='OpenRoom',
    version='v1.0',
    lifespan=lifespan
)

app.include_router(account_router)
app.include_router(users_router)
app.include_router(user_groups_router)
app.include_router(buildings_router)
app.include_router(units_router)
app.include_router(rooms_router)
app.include_router(room_groups_router)
app.include_router(events_router)
app.include_router(invites_router)
app.include_router(registrations_router)
app.include_router(permissions_router)
app.include_router(organization_router)



@app.get("/")
async def mainpage():
    return {"status": "working"}



if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="debug", reload=True)
