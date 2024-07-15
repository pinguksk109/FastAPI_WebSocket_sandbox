from app.repository.ai_client import AIClient

class ClaudeClient(AIClient):
    def get_response(self, message: str) -> str:
        return f"Claude Response to: {message}"
