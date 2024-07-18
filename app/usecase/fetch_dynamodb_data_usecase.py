from app.domain.organization import Organization
from app.infrastructure.repository.dynamodb_repository import DynamoDBRepository

class FetchDynamoDBDataUseCase:
    def __init__(self, repository):
        self.repository = repository

    async def execute(self):
        organization = await self.repository.fetch_data()
        return organization