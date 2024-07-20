from app.domain.organization import Organization
from app.infrastructure.repository.dynamodb_repository import DynamoDBRepository
import logging

logger = logging.getLogger(__name__)

class FetchDynamoDBDataUseCase:
    def __init__(self, dynamodb_repository: DynamoDBRepository):
        self.repository = dynamodb_repository

    async def execute(self) -> Organization:
        try:
            organization = await self.repository.fetch_data()
            return organization
        except Exception as e:
            logger.error(f"Error in FetchDynamoDBDataUseCase: {e}")
            raise