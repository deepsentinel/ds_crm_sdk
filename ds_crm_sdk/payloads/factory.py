"""
Factory module for creating payload builders based on client type.
"""
from ds_crm_sdk.constants import ClientOrigin
from .request_models import WebPayloadBase, EWAPPayloadBase, MobileAPIPayloadBase, AdminDashboardPayloadBase


def get_main_payload_builder(client_origin: str):
    """
    Factory function to get the main payload builder based on the client type.
    :param client_origin: The type of client for which the payload is being built.
    :return: An instance of the appropriate payload builder.
    """
    if client_origin == ClientOrigin.WEB:
        return WebPayloadBase()
    if client_origin == ClientOrigin.EWAP:
        return EWAPPayloadBase()
    if client_origin == ClientOrigin.MOBILE_API:
        return MobileAPIPayloadBase()
    if client_origin == ClientOrigin.ADMIN_DASHBOARD:
        return AdminDashboardPayloadBase()
    raise ValueError(f"Unsupported client origin: {client_origin}")
