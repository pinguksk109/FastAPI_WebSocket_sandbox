from app.domain.organization import Organization

class DynamoDBRepository:
    async def fetch_data(self):
        mock_data = {"limit": 100, "count": 10}
        return Organization(limit=mock_data['limit'], count=mock_data['count'])