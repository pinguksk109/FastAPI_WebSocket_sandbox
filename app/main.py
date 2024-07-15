from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.websocket_router import router as websocket_router

app = FastAPI()

app.include_router(websocket_router, prefix="/ws")