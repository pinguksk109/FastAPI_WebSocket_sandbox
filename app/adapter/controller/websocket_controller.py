import json
import logging
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.service.websocket_service import WebSocketService
from app.factory.ai_client_factory import AIClientFactory
from app.repository.ai_client_type import AIClientType
from app.service.ai_service import AiService

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

@router.websocket("/ai_test")
async def ai_endpoint(websocket: WebSocket, client_type: AIClientType = AIClientType.GEMINI):
    await websocket.accept()
    logger.info("WebSocket通信接続開始")

    ai_client = AIClientFactory.create_client(client_type)
    ai_service = AiService(ai_client)

    try:
        while True:
            request = await websocket.receive_text()
            requestBody = json.load(request)

            id = requestBody.get("id")
            message_content = request.get("message")
            number = requestBody.get("number")

            if len(id) > 100 or len(message_content) > 100:
                await websocket.send_json({"error": "ID and message must be 100 characters or less"}, status_code=400)
                continue

            if number >= 10:
                await websocket.send_json({"error": "Number must be less than 10"}, status_code=400)
                continue

            logger.info(f"Received message: {request}")
            response = ai_service.process_message(request)
            await websocket.send_text(response)
            logger.info(f"Sent response: {response}")
    except WebSocketDisconnect:
        logger.info("WebSocket connection closed")
    except Exception as e:
        logger.error(f"Error: {e}")
        await websocket.close()          