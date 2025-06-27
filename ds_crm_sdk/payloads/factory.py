"""
Factory module for creating payload builders based on client type.
"""
from ds_crm_sdk.constants import ClientOrigin
from .request_models import WebPayloadBase, EWAPPayloadBase, MobileAPIPayloadBase, AdminDashboardPayloadBase
from .base import PayloadBuilder


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


class MainPayloadBuilder(PayloadBuilder):
    """
    MainPayloadBuilder is responsible for constructing the main payload
    """
    def __init__(self, client_origin: ClientOrigin):
        """
        Initialize the MainPayloadBuilder with the client type.
        :param client_origin: The type of client for which the payload is being built.
        """
        self.client_origin = client_origin

    def build_main_payload(self, **extra) -> dict:
        """
        Build and return the payload as a Pydantic model based on the client type.
        :param extra: Additional parameters that may be needed for the payload.
        :return: An instance of the appropriate payload model (pydantic basemodel)
        """
        payload_container = get_main_payload_builder(client_origin=self.client_origin)
        if extra:
            for key, value in extra.items():
                if not hasattr(payload_container, key):
                    # If the key exists in the payload model, set its value
                    raise ValueError(f"Invalid key '{key}' for payload model {payload_container.__class__.__name__}")
                if value is None:
                    continue
                setattr(payload_container, key, value)
        return payload_container.model_dump(exclude_none=True)  # Exclude None values from the payload

