class UseCaseManager:
    def __init__(self, fetch_data_usecase, fetch_dynamodb_data_usecase, request_chatapi_usecase):
        self.fetch_data_usecase = fetch_data_usecase
        self.fetch_dynamodb_data_usecase = fetch_dynamodb_data_usecase
        self.request_chatapi_usecase = request_chatapi_usecase

    async def handle_message(self, message: str):
        pass