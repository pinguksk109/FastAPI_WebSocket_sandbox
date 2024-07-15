from app.model.message import Message

class WebSocketRepository:
    def get_response(self, message: Message) -> Message:
        return Message(content=f"Mock response to: {message.content}")