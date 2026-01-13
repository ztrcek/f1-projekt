from fastapi import FastAPI
from app.api import home  # uvozi home router

app = FastAPI(title="F1 Backend API")

app.include_router(home.router)  # vključimo /home endpoint

@app.get("/")
async def root():
    return {"message": "F1 Backend running!"}
