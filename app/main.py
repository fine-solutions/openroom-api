import uvicorn
from fastapi import FastAPI

from api.routers import (
    account_router, 
    events_router
    )




app = FastAPI(
    title='OpenRoom',
    version='v1.0',
)



app.include_router(account_router)
app.include_router(events_router)



@app.get("/")
async def mainpage():
    return {"status": "working"}



if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="debug")
