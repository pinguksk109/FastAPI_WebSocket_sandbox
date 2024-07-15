import logging
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.service.websocket_service import WebSocketService

router = APIRouter()
logger = logging.getLogger(__name__)

@router.websocket("/test")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websocket_service = WebSocketService()
    try:
        while True:
            request = await websocket.receive_text()
            logger.info(f"Received message: {request}")
            response = websocket_service.process_message(request)
            # await websocket_service.process_message(request)
            await websocket.send_text(request)
            logger.info(f"Sent response: {response}")
    except WebSocketDisconnect:
        logger.info("WebSocket connection closed")
    except Exception as e:
        logger.error(f"Error: {e}")
        await websocket.close()