from fastapi import APIRouter, WebSocket
# from app.services.websocket_service import WebSocketService

router = APIRouter()

@router.websocket("/endpoint")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # websocket_service = WebSocketService()
    while True:
        data = await websocket.receive_text()
        # response = websocket_service.process_message(data)
        await websocket.send_text('hoge')