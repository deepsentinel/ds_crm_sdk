"""
Base class for CRM HTTP clients.
"""
from ds_crm_sdk.payloads import PayloadBuilder
from ds_crm_sdk.constants import ClientOrigin


class BaseCRMClient:
    """
    Base class for CRM HTTP clients.
    This class should be extended by specific CRM clients to implement the required methods.
    """

    def __init__(self, builder: PayloadBuilder, base_url: str):
        self._builder = builder
        self._base_url = base_url

    def _build_endpoint_url(self, endpoint_template: str, values_to_inject: dict = None) -> str:
        """
        Build the full endpoint URL by injecting values into the endpoint template.
        :param endpoint_template: The endpoint template string with placeholders.
        :param values_to_inject: A list of values to inject into the endpoint template.
        :return: The full endpoint URL as a string.
        """
        if values_to_inject is None:
            return self._base_url + endpoint_template
        return self._base_url + endpoint_template.format(**values_to_inject)

    def _build_main_params(self, **extra) -> dict:
        """
        Build the main parameters for the request payload.
        :param extra: Additional parameters that may be needed for the payload.
        :return: A dictionary containing the main payload parameters.
        """
        return self._builder.build_main_payload(**extra)

    @staticmethod
    def _build_custom_client_origin(client_origin: ClientOrigin) -> dict:
        """
        Build the custom client origin for the request payload.
        :param client_origin: The origin of the client making the request.
        :return: A dictionary containing the client origin.
        """
        return {'X-Client-Origin': client_origin} if client_origin else {}
