import unittest
from unittest.mock import patch
from http import HTTPStatus
from ds_crm_sdk.clients.http.crm_client import CRMClient
from ds_crm_sdk.transports.http import DSHTTPTransport
from ds_crm_sdk.constants import ClientOrigin
from ds_crm_sdk.clients.http.endpoints import AccountEndpoint, AccountTypesEndpoint
from ds_crm_sdk.constants import SortOrder
from tests.fixtures import DummyAccountFactory, DummyAccountTypeFactory


class TestHTTPCRMClient(unittest.TestCase):
    def setUp(self):
        self.request_token = 'Dummy Token'
        self.transport = DSHTTPTransport(token_provider=lambda: self.request_token)
        self.base_url = 'https://ds-mock-crm-service.com'
        self.client = CRMClient(
            client_origin=ClientOrigin.EWAP,
            base_url=self.base_url,
            transport=self.transport
        )
        self.patcher = patch('requests.request')
        self.mock_request = self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def test_get_account(self):
        # Mock the response with status and return data
        self.mock_request.return_value.status_code = HTTPStatus.OK
        # Generate a dummy account using the factory
        account = DummyAccountFactory()
        self.mock_request.return_value.json.return_value = {'account': account.to_dict()}

        # Trigger the request
        data, status_code = self.client.get_account(account_id=str(account.id))
        self.mock_request.assert_called_once()
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

    def test_get_accounts(self):
        # Mock the response with status and return data
        self.mock_request.return_value.status_code = HTTPStatus.OK
        # Generate a list of dummy accounts using the factory
        accounts = [DummyAccountFactory() for _ in range(5)]
        patched_email = 'same_email@xyz.com'
        _ = [
            account for index, account in enumerate(accounts)
            if not index % 2 and setattr(account, 'email_address', patched_email) is None
        ]
        filtered_accounts = [account for account in accounts if account.email_address == patched_email]
        expected_response = {'accounts': [account.to_dict() for account in filtered_accounts]}
        self.mock_request.return_value.json.return_value = expected_response
        # Trigger the request
        filters = {'email': patched_email}
        data, status_code = self.client.get_accounts(offset=0, limit=5, sort_by='created',
                                                     filters=filters,
                                                     sort_order=SortOrder.DESC)
        self.mock_request.assert_called_once()
        args, kwargs = self.mock_request.call_args
        headers = kwargs.get('headers', {})
        params = kwargs.get('params', {})
        print(params)
        complete_url = f"{self.base_url}{AccountEndpoint.ACCOUNTS.value}"

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

    def test_get_account_types(self):
        # Mock the response with status and return data
        self.mock_request.return_value.status_code = HTTPStatus.OK
        # Generate a list of dummy account types using the factory
        account_types = [DummyAccountTypeFactory().to_dict() for _ in range(3)]
        self.mock_request.return_value.json.return_value = {'account_types': account_types}

        # Trigger the request
        data, status_code = self.client.get_account_types(limit=3, offset=0)
        self.mock_request.assert_called_once()
        args, kwargs = self.mock_request.call_args
        headers = kwargs.get('headers', {})
        params = kwargs.get('params', {})
        complete_url = f"{self.base_url}{AccountTypesEndpoint.ACCOUNT_TYPES.value}"

        # Assertions
        self.assertEqual(kwargs['method'], 'GET')
        self.assertEqual(headers['Authorization'], self.request_token)
        self.assertEqual(params['client_origin'], ClientOrigin.EWAP)
        self.assertEqual(kwargs['url'], complete_url)
        self.assertEqual(status_code, HTTPStatus.OK)
        self.assertEqual(data['account_types'], account_types)

    def test_get_account_type(self):
        # Mock the response with status and return data
        self.mock_request.return_value.status_code = HTTPStatus.OK
        # Generate a dummy account type using the factory
        account_type = DummyAccountTypeFactory()
        self.mock_request.return_value.json.return_value = {'account_type': account_type.to_dict()}
        # Trigger the request
        data, status_code = self.client.get_account_type(type_id=account_type.id)
        self.mock_request.assert_called_once()
        args, kwargs = self.mock_request.call_args
        headers = kwargs.get('headers', {})
        params = kwargs.get('params', {})
        complete_url = f"{self.base_url}{AccountTypesEndpoint.ACCOUNT_TYPE.format(type_id=account_type.id)}"
        # Assertions
        self.assertEqual(kwargs['method'], 'GET')
        self.assertEqual(headers['Authorization'], self.request_token)
        self.assertEqual(params['client_origin'], ClientOrigin.EWAP)
        self.assertEqual(kwargs['url'], complete_url)
        self.assertEqual(status_code, HTTPStatus.OK)
        self.assertEqual(data['account_type'], account_type.to_dict())

# Note: Above 4 tests are sufficient to cover the basic functionality of the CRMClient.
