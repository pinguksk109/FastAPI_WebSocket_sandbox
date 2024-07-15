from app.repository.websocket_repository import WebSocketRepository
from app.model.message import Message

class WebSocketService:
    def __init__(self):
        self.repository = WebSocketRepository()

    def process_message(self, message_text: str) -> str:
        message = Message(content=message_text)
        response_message = self.repository.get_response(message)
        return response_message.content