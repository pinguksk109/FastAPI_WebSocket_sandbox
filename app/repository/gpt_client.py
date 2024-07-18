from app.repository.ai_client import AIClient

class GPTClient(AIClient):
    def get_response(self, message: str) -> str:
        return f"GPT Response to: {message}"
