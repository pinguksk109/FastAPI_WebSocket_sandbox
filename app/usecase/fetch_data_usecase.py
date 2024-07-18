class FetchDataUseCase:
    def __init__(self, repository):
        self.repository = repository

    async def execute(self):
        response = await self.repository.fetch_data()
        if response.status_code == 200:
            pass
        else:
            pass