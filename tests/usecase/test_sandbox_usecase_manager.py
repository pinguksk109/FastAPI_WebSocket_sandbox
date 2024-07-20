# import unittest
# from unittest.mock import AsyncMock, Mock
# from app.usecase.fetch_data_usecase import FetchDataUseCase
# from app.usecase.fetch_dynamodb_data_usecase import FetchDynamoDBDataUseCase
# from app.usecase.request_chatapi_usecase import RequestChatApiUseCase
# from app.usecase.usecase_manager import UseCaseManager
# from app.domain.organization import Organization
# from app.domain.article import Article
# from app.domain.sandbox_output import SandboxOutput
# import asyncio

# class TestUseCaseManager(unittest.IsolatedAsyncioTestCase):
#     def setUp(self):
#         self.fetch_data_usecase = Mock(spec=FetchDataUseCase)
#         self.fetch_dynamodb_data_usecase = Mock(spec=FetchDynamoDBDataUseCase)
#         self.request_chatapi_usecase = Mock(spec=RequestChatApiUseCase)
#         self.output = Mock(spec=SandboxOutput)

#         self.organization = Organization(limit=100, count=10)
#         self.article = Article(content="Test Article")

#         self.fetch_dynamodb_data_usecase.execute = AsyncMock(return_value=self.organization)
#         self.request_chatapi_usecase.execute = AsyncMock(return_value=self.article)

#         self.manager = UseCaseManager(
#             fetch_data_usecase=self.fetch_data_usecase,
#             fetch_dynamodb_data_usecase=self.fetch_dynamodb_data_usecase,
#             request_chatapi_usecase=self.request_chatapi_usecase,
#             output=self.output
#         )

#     async def test_handle_message_success(self):
#         message = "test message"

#         result = await self.manager.handle_message(message)

#         self.fetch_dynamodb_data_usecase.execute.assert_called_once()
#         self.request_chatapi_usecase.execute.assert_called_once_with(message)
#         self.output.set_organization.assert_called_once_with(self.organization)
#         self.output.set_article.assert_called_once_with(self.article)

#         self.assertEqual(result, self.output)

#     async def test_handle_message_fetch_dynamodb_data_usecase_error(self):
#         self.fetch_dynamodb_data_usecase.execute = AsyncMock(side_effect=Exception("FetchDynamoDBDataUseCase error"))
#         message = "test message"

#         result = await self.manager.handle_message(message)

#         self.output.set_organization.assert_called_once_with(None)
#         self.output.set_article.assert_called_once_with(self.article)
#         self.assertEqual(result, self.output)

#     async def test_handle_message_request_chatapi_usecase_error(self):
#         self.request_chatapi_usecase.execute = AsyncMock(side_effect=Exception("RequestChatApiUseCase error"))
#         message = "test message"

#         result = await self.manager.handle_message(message)

#         self.output.set_organization.assert_called_once_with(self.organization)
#         self.output.set_article.assert_called_once_with(None)
#         self.assertEqual(result, self.output)

# if __name__ == "__main__":
#     unittest.main()
