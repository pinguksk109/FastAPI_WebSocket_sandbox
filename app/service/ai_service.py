from app.repository.ai_client import  AIClient

class AiService:
    def __init__(self, ai_client: AIClient):
        self.ai_client = ai_client
    
    def process_message(self, message_text: str) -> str:
        return self.ai_client.get_response(message_text)