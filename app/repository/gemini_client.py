from app.repository.ai_client import AIClient

class GeminiClient(AIClient):
    def get_response(self, message: str) -> str:
        return f"Gemini Response to: {message}"
