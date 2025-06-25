from .main_payload import WebPayloadBase, EwapPayloadBase, MobileAPIPayloadBase, AdminDashboardPayloadBase
from .base import PayloadBuilder
from pydantic import BaseModel
from ds_crm_sdk.constants import ClientOrigin


def get_main_payload_builder(client_origin: str):
    """
    Factory function to get the main payload builder based on the client type.
    :param client_origin: The type of client for which the payload is being built.
    :return: An instance of the appropriate payload builder.
    """
    if client_origin == ClientOrigin.WEB:
        return WebPayloadBase()
    elif client_origin == ClientOrigin.EWAP:
        return EwapPayloadBase()
    elif client_origin == ClientOrigin.MOBILE_API:
        return MobileAPIPayloadBase()
    elif client_origin == ClientOrigin.ADMIN_DASHBOARD:
        return AdminDashboardPayloadBase()
    else:
        raise ValueError(f"Unsupported client origin: {client_origin}")


class MainPayloadBuilder(PayloadBuilder):
    def build_main_payload(self, client_type: str) -> BaseModel:
        """
        Build and return the payload as a Pydantic model based on the client type.
        :param client_type: The type of client for which the payload is being built.
        :return: An instance of the appropriate payload model (pydantic basemodel)
        """
        return get_main_payload_builder(client_origin=client_type)
