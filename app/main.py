import logging
from fastapi import FastAPI, WebSocket
from app.adapter.controller import websocket_controller
from app.adapter.controller.sandbox_controller import SandboxController

# ログの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

sandbox_controller = SandboxController()

@app.websocket("/sandbox")
async def websocket_endpoint(websocket: WebSocket):
    await sandbox_controller.handle_websocket(websocket)

app.include_router(websocket_controller.router)
