from abc import ABC, abstractmethod

class AIClient(ABC):
    @abstractmethod
    def get_response(self, message: str) -> str:
        pass