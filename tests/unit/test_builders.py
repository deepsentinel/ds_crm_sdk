import unittest
from ds_crm_sdk.payloads.factory import get_main_payload_builder
from ds_crm_sdk.constants import ClientOrigin
from ds_crm_sdk.payloads.base_request_models import (WebPayloadBase, EWAPPayloadBase,
                                                     MobileAPIPayloadBase, AdminDashboardPayloadBase)


class TestBuilder(unittest.TestCase):
    def setUp(self):
        pass

    def test_different_client_origin_payload_builder(self):
        """
        Test the factory function to ensure it returns the correct payload builder
        :return:
        """
        # Test for Web client origin
        payload = get_main_payload_builder(ClientOrigin.WEB)
        self.assertIsInstance(payload, WebPayloadBase)
        self.assertEqual(payload.client_origin, ClientOrigin.WEB)

        # Test for EWAP client origin
        payload = get_main_payload_builder(ClientOrigin.EWAP)
        self.assertIsInstance(payload, EWAPPayloadBase)
        self.assertEqual(payload.client_origin, ClientOrigin.EWAP)

        # Test for Mobile API client origin
        payload = get_main_payload_builder(ClientOrigin.MOBILE_API)
        self.assertIsInstance(payload, MobileAPIPayloadBase)
        self.assertEqual(payload.client_origin, ClientOrigin.MOBILE_API)

        # Test for Admin Dashboard client origin
        payload = get_main_payload_builder(ClientOrigin.ADMIN_DASHBOARD)
        self.assertIsInstance(payload, AdminDashboardPayloadBase)
        self.assertEqual(payload.client_origin, ClientOrigin.ADMIN_DASHBOARD)

        # Test for unsupported client origin
        with self.assertRaises(ValueError):
            get_main_payload_builder("unsupported_origin")