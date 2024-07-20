from fastapi import WebSocket
import logging

from app.domain.sandbox_output import SandboxOutput
from app.infrastructure.repository.chatapi_repository import ChatApiRepository
from app.infrastructure.repository.dynamodb_repository import DynamoDBRepository
from app.infrastructure.repository.external_api_repository import ExternalApiRepository
from app.response.sandbox_response import ArticleResponse, OrganizationResponse, SandboxResponse
from app.usecase.fetch_data_usecase import FetchDataUseCase
from app.usecase.fetch_dynamodb_data_usecase import FetchDynamoDBDataUseCase
from app.usecase.request_chatapi_usecase import RequestChatApiUseCase
from app.usecase.usecase_manager import UseCaseManager

logger = logging.getLogger(__name__)

class SandboxController:
    def __init__(self):
        fetch_data_usecase = FetchDataUseCase(ExternalApiRepository())
        fetch_dynamodb_data_usecase = FetchDynamoDBDataUseCase(DynamoDBRepository())
        request_chatapi_usecase = RequestChatApiUseCase(ChatApiRepository())
        self.manager = UseCaseManager(fetch_data_usecase, fetch_dynamodb_data_usecase, request_chatapi_usecase, SandboxOutput())

    async def handle_websocket(self, websocket: WebSocket):
        await websocket.accept()
        try:
            while True:
                request = await websocket.receive_text()
                output = await self.manager.handle_message(request)

                response = SandboxResponse(
                    organization=OrganizationResponse(
                        limit=output.get_organization().limit,
                        count=output.get_organization().count
                    ) if output.get_organization() else None,
                    article=ArticleResponse(
                        content=output.get_article().content
                    ) if output.get_article() else None
                )

                await websocket.send_json(response.dict())
        except Exception as e:
            logger.error(f"Connection closed: {e}", exc_info=True)
        finally:
            await websocket.close()