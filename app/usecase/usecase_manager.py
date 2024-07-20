from app.usecase.fetch_data_usecase import FetchDataUseCase
from app.usecase.fetch_dynamodb_data_usecase import FetchDynamoDBDataUseCase
from app.usecase.request_chatapi_usecase import RequestChatApiUseCase
from app.domain.sandbox_output import SandboxOutput
import logging

logger = logging.getLogger(__name__)

class UseCaseManager:
    def __init__(self, fetch_data_usecase: FetchDataUseCase, fetch_dynamodb_data_usecase : FetchDynamoDBDataUseCase, request_chatapi_usecase: RequestChatApiUseCase, output: SandboxOutput):
        self.fetch_data_usecase = fetch_data_usecase
        self.fetch_dynamodb_data_usecase = fetch_dynamodb_data_usecase
        self.request_chatapi_usecase = request_chatapi_usecase
        self.output = output

    async def handle_message(self, message: str):
        try:
            fetch_dynamodb_data_result = await self.fetch_dynamodb_data_usecase.execute()
        except Exception as e:
            logger.error(f"Error in FetchDynamoDBDataUseCase: {e}", exc_info=True)
            fetch_dynamodb_data_result = None

        try:
            chatapi_response = await self.request_chatapi_usecase.execute(message)
        except Exception as e:
            logger.error(f"Error in RequestChatApiUseCase: {e}", exc_info=True)
            chatapi_response = None

        try:      
            self.output.set_organization(fetch_dynamodb_data_result)
            self.output.set_article(chatapi_response)
        except Exception as e:
            logger.error(f"Error in output: {e} {fetch_dynamodb_data_result.count} {fetch_dynamodb_data_result.limit} {chatapi_response.content}", exc_info=True)

        return self.output