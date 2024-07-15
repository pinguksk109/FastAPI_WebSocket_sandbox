import logging
from fastapi import FastAPI
from app.adapter.controller import websocket_controller

# ログの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(websocket_controller.router)
