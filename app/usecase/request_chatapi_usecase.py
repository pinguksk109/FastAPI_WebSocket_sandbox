class RequestChatApiUseCase:
    def __init__(self, repository):
        self.repository = repository
    
    async def execute(self, article: str):
        response = await self.repository.request_gpt(article)
        return response