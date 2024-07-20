from app.domain.organization import Organization
from app.infrastructure.repository import dynamodb_repository

class FetchDataUseCase:
    def __init__(self, dynamodb_repository: dynamodb_repository):
        self.dynamodb_repository = dynamodb_repository

    async def execute(self):
        organization = await self.dynamodb_repository.fetch_data()
        return organization