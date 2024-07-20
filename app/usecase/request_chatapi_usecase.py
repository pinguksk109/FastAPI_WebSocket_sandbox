from app.domain.article import Article
from app.infrastructure.repository.chatapi_repository import ChatApiRepository
import logging

logger = logging.getLogger(__name__)

class RequestChatApiUseCase:
    def __init__(self, chatapi_repository: ChatApiRepository):
        self.chatapi_repository = chatapi_repository
    
    async def execute(self, article: str) -> Article:
        try:
            chatapi_response = await self.chatapi_repository.request_chatapi(article)
            return chatapi_response
        except Exception as e:
            logger.error(f"Error in RequestChatApiUseCase: {e}", exc_info=True)
            raise