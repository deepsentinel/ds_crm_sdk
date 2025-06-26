import unittest
from unittest.mock import AsyncMock, MagicMock
from ds_crm_sdk.http_clients.crm_client import CRMClient
from ds_crm_sdk.payloads import MainPayloadBuilder
from ds_crm_sdk.transports import DSHTTPTransport
from ds_crm_sdk.constants import ClientOrigin


class TestHTTPCRMClient(unittest.TestCase):
    def setUp(self):
        self.builder = MainPayloadBuilder()
        self.mock_transport = MagicMock(spec=DSHTTPTransport)
        self.base_url = 'https://mock-crm-service.com'
        self.client = CRMClient(
            client_origin=ClientOrigin.EWAP,
            builder=self.builder,
            base_url=self.base_url,
            transport=self.mock_transport
        )

    def test_get_account(self):
        # Mock the transport response
        self.mock_transport.send.return_value = ({"id": "123", "name": "Test Account"}, 200)

        # Call the method
        account_id = "123"
        data, status_code = self.client.get_account(account_id)

        # Assertions
        self.mock_transport.send.assert_called_once()
        self.assertEqual(status_code, 200)
        self.assertEqual(data["id"], "123")

    def test_get_account_types(self):
        # Mock the transport response
        self.mock_transport.send.return_value = ([{"type": "Business"}, {"type": "Personal"}], 200)

        # Call the method
        data, status_code = self.client.get_account_types()

        # Assertions
        self.mock_transport.send.assert_called_once()
        self.assertEqual(status_code, 200)
        self.assertEqual(len(data), 2)


if __name__ == "__main__":
    unittest.main()