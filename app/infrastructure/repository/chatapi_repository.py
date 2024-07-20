from app.domain.article import Article
import logging

logger = logging.getLogger(__name__)

class ChatApiRepository:
    async def request_chatapi(self, article: str):
        try:
            return Article(content="GPT response")
        except Exception as e:
            logger.error(f"Error in ChatApiRepository: {e}", exc_info=True)
            raise