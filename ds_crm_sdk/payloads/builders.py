"""
MainPayloadBuilder is responsible for constructing the main payload
"""
from ds_crm_sdk.constants import ClientOrigin
from .base import PayloadBuilder
from .factory import get_main_payload_builder


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
        payload = payload_container.model_dump(exclude_none=True, mode='json')  # Exclude None values from the payload
        if 'filters' in payload and isinstance(payload['filters'], dict):
            payload.update({**payload.pop('filters')})
        return payload
