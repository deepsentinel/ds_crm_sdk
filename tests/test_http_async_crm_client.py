import unittest
from unittest.mock import AsyncMock, patch
from http import HTTPStatus
from ds_crm_sdk.clients.http.async_crm_client import AsyncCRMClient
from ds_crm_sdk.payloads import MainPayloadBuilder
from ds_crm_sdk.transports.http import DSAsyncHTTPTransport
from ds_crm_sdk.constants import ClientOrigin, SortOrder
from tests.fixtures import DummyAccountFactory
from ds_crm_sdk.clients.http.endpoints import AccountEndpoint


class TestAsyncHTTPCRMClient(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.builder = MainPayloadBuilder()
        self.request_token = 'Dummy Token'
        self.transport = DSAsyncHTTPTransport(token_provider=lambda: self.request_token)
        self.base_url = 'https://ds-mock-crm-service.com'
        self.client = AsyncCRMClient(
            base_url=self.base_url,
            client_type=ClientOrigin.EWAP,
            transport=self.transport,
            builder=self.builder
        )
        self.patcher = patch('httpx.AsyncClient.request')
        self.mock_request = self.patcher.start()
        self.addCleanup(self.patcher.stop)

    async def test_get_account(self):
        # Mock the response with status and return data
        self.mock_request.return_value.status_code = HTTPStatus.OK
        account = DummyAccountFactory()
        self.mock_request.return_value.json = AsyncMock(return_value={'account': account.to_dict()})

        # Trigger the request
        data, status_code = await self.client.get_account(account_id=str(account.id))
        self.mock_request.assert_awaited_once()
        args, kwargs = self.mock_request.call_args
        headers = kwargs.get('headers', {})
        params = kwargs.get('params', {})
        complete_url = f"{self.base_url}{AccountEndpoint.SPECIFIC_ACCOUNT.format(account_id=account.id)}"

        # Assertions
        self.assertEqual(kwargs['method'], 'GET')
        self.assertEqual(headers['Authorization'], self.request_token)
        self.assertEqual(params['client_origin'], ClientOrigin.EWAP)
        self.assertEqual(kwargs['url'], complete_url)
        self.assertEqual(status_code, HTTPStatus.OK)
        self.assertEqual(data['account']['id'], account.id)

    async def test_get_accounts(self):
        # Mock the response with status and return data
        self.mock_request.return_value.status_code = HTTPStatus.OK
        accounts = [DummyAccountFactory() for _ in range(5)]
        patched_email = 'same_email@xyz.com'
        _ = [
            account for index, account in enumerate(accounts)
            if not index % 2 and setattr(account, 'email_address', patched_email) is None
        ]
        filtered_accounts = [account for account in accounts if account.email_address == patched_email]
        expected_response = {'accounts': [account.to_dict() for account in filtered_accounts]}
        self.mock_request.return_value.json = AsyncMock(return_value=expected_response)

        # Trigger the request
        filters = {'email': patched_email}
        data, status_code = await self.client.get_accounts(offset=0, limit=5, sort_by='created',
                                                           filters=filters,
                                                           sort_order=SortOrder.DESC)
        self.mock_request.assert_awaited_once()
        args, kwargs = self.mock_request.call_args
        headers = kwargs.get('headers', {})
        params = kwargs.get('params', {})
        complete_url = f"{self.base_url}{AccountEndpoint.BASE}"

        # Assertions
        self.assertEqual(len(data['accounts']), len(filtered_accounts))
        for key, value in filters.items():
            self.assertIn(key, params, msg=f"Missing key: {key}")
            self.assertEqual(params[key], value, msg=f"Mismatch for key: {key}")
        self.assertEqual(kwargs['method'], 'GET')
        self.assertEqual(headers['Authorization'], self.request_token)
        self.assertEqual(params['client_origin'], ClientOrigin.EWAP)
        self.assertEqual(params['offset'], 0)
        self.assertEqual(params['limit'], 5)
        self.assertEqual(params['sort_by'], 'created')
        self.assertEqual(params['sort_order'], SortOrder.DESC)
        self.assertEqual(kwargs['url'], complete_url)
        self.assertEqual(status_code, HTTPStatus.OK)
        self.assertEqual(data['accounts'], expected_response['accounts'])

# Note: Above 2 tests are sufficient to cover the basic functionality of the AsyncCRMClient.
