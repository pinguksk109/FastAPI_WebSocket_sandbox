from app.domain.article import Article

class ChatApiRepository:
    async def request_chatapi(self, article: str):
        return Article(content="GPT response")