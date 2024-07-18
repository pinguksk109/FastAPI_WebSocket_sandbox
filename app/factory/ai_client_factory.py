from app.repository.ai_client import AIClient
from app.repository.gpt_client import GPTClient
from app.repository.gemini_client import GeminiClient
from app.repository.claude_client import ClaudeClient
from app.repository.ai_client_type import AIClientType

class AIClientFactory:
    @staticmethod
    def create_client(client_type: AIClientType) -> AIClient:
        if client_type == AIClientType.GPT:
            return GPTClient()
        elif client_type == AIClientType.GEMINI:
            return GeminiClient()
        elif client_type == AIClientType.CLAUDE:
            return ClaudeClient()
        else:
            raise ValueError(f"Unknown client type: {client_type}")