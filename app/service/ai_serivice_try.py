'''
実験用:使わないクラス
'''

from enum import Enum
import logging

logger = logging.getLogger(__name__)

class AIClientType(Enum):
    GPT = "gpt"
    GEMINI = "gemini"
    CLAUDE = "claude"

class AiService:
    def __init__(self, client_type: AIClientType):
        self.client_type = client_type

    def process_message(self, message: str) -> str:
        if self.client_type == AIClientType.GPT:
            client = GPTClient()
        elif self.client_type == AIClientType.GEMINI:
            client = GeminiClient()
        elif self.client_type == AIClientType.CLAUDE:
            client = ClaudeClient()
        else:
            raise ValueError(f"Unknown client type: {self.client_type}")

        response = client.process_message(message)
        return response

class GPTClient:
    def process_message(self, message: str) -> str:
        return "Response from GPT model"

class GeminiClient:
    def process_message(self, message: str) -> str:
        return "Response from Gemini model"

class ClaudeClient:
    def process_message(self, message: str) -> str:
        return "Response from Claude model"