from .main_payload import WebPayloadBase, EwapPayloadBase, MobileAPIPayloadBase, AdminDashboardPayloadBase
from .base import PayloadBuilder
from pydantic import BaseModel


def get_main_payload_builder(client_type: str):
    """
    Factory function to get the main payload builder based on the client type.
    :param client_type: The type of client for which the payload is being built.
    :return: An instance of the appropriate payload builder.
    """
    if client_type == 'web':
        return WebPayloadBase()
    elif client_type == 'ewap':
        return EwapPayloadBase()
    elif client_type == 'mobile-api':
        return MobileAPIPayloadBase()
    elif client_type == 'admin-dashboard':
        return AdminDashboardPayloadBase()
    else:
        raise ValueError(f"Unsupported client type: {client_type}")


class MainPayloadBuilder(PayloadBuilder):
    def build_main_payload(self, client_type: str) -> BaseModel:
        """
        Build and return the payload as a Pydantic model based on the client type.
        :param client_type: The type of client for which the payload is being built.
        :return: An instance of the appropriate payload model (pydantic basemodel)
        """
        return get_main_payload_builder(client_type=client_type)
