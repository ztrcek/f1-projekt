# v app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.home import router as home_router

app = FastAPI(title="F1 Backend API")

origins = [
    "http://127.0.0.1:5500",  # če boš uporabljal live server
    "http://localhost:5500",
    "*",  # za testiranje lahko dovoliš vse, kasneje omeji
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(home_router, prefix="/home")

@app.get("/")
async def root():
    return {"message": "F1 Backend running!"}
