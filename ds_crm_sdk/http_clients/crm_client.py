from ds_crm_sdk.transports.base import HTTPMethod, HTTPTransport
from ds_crm_sdk.payloads import MainPayloadBuilder
from .endpoints import AccountEndpoint, AccountAddressEndpoint, AccountTypesEndpoint
from ds_crm_sdk.constants import ClientOrigin, SortOrder


class CRMClient:
    def __init__(self, base_url: str, client_origin: ClientOrigin, transport: HTTPTransport, builder: MainPayloadBuilder):
        self.__base_url = base_url
        self.__client_origin = client_origin
        self.__transport = transport
        self.__builder = builder
        # Creates the main payload based on the client type (skeleton)
        self.__main_payload = self.__builder.build_main_payload(client_type=self.__client_origin)

    def get_account(self, account_id: str) -> tuple:
        """
        Get account details by account ID.
        :param account_id: The ID of the account to retrieve.
        :return: Account details as a dictionary with http status code.
        """
        endpoint = AccountEndpoint.SPECIFIC_ACCOUNT.format(account_id=account_id)
        data, status_code = self.__transport.send(
            method=HTTPMethod.GET,
            endpoint=self.__base_url + endpoint,
            params=self.__main_payload.dict()
        )
        return data, status_code

    def get_accounts(self, filters: dict = None, offset=0, limit=10,
                     sort_by: str = 'created', sort_order: SortOrder = SortOrder.DESC) -> tuple:
        """
        Get accounts with filters.
        :param filters: A dictionary containing the filters to apply (optional).
        :param offset: Starting point for pagination, default is 0.
        :param limit: The number of accounts per page for pagination.
        :param sort_by: The field to sort by, default is 'created'.
        :param sort_order: The order of sorting, default is descending (DESC).
        :return: A list of accounts matching the filters with http status code
        """
        endpoint = AccountEndpoint.BASE
        params = {**self.__main_payload.dict(), 'offset': offset, 'limit': limit,
                  'sort_by': sort_by, 'sort_order': sort_order}
        if filters and isinstance(filters, dict):
            params.update(filters)
        data, status_code = self.__transport.send(
            method=HTTPMethod.GET,
            endpoint=self.__base_url + endpoint,
            params=params
        )
        return data, status_code

    def get_account_addresses(self, account_id: str, filters: dict = None, offset=0, limit=10,
                              sort_by: str = 'address.created',
                              sort_order: SortOrder = SortOrder.DESC) -> tuple:
        """
        Get addresses for a specific account.
        :param account_id: The ID of the account whose addresses are to be retrieved.
        :param filters: A dictionary containing the filters to apply (optional).
        :param offset: Starting point for pagination, default is 0.
        :param limit: The number of addresses per page for pagination.
        :param sort_by: The field to sort by, default is 'address.created'.
        :param sort_order: The order of sorting, default is descending (DESC).
        :return: A list of addresses associated with the account with http status code.
        """
        endpoint = AccountAddressEndpoint.ACCOUNT_ADDRESSES.format(account_id=account_id)
        params = {**self.__main_payload.dict(), 'offset': offset, 'limit': limit,
                  'sort_by': sort_by, 'sort_order': sort_order}
        if filters and isinstance(filters, dict):
            params.update(filters)
        data, status_code = self.__transport.send(
            method=HTTPMethod.GET,
            endpoint=self.__base_url + endpoint,
            params=params
        )
        return data, status_code

    def get_account_address(self, account_id: str, address_id: str) -> tuple:
        """
        Get addresses for a specific account.
        :param account_id: The ID of the account whose addresses are to be retrieved.
        :param address_id: The ID of the address to retrieve.
        :return: A list of addresses associated with the account with http status code.
        """
        endpoint = AccountAddressEndpoint.ACCOUNT_ADDRESS.format(account_id=account_id, address_id=address_id)
        params = {**self.__main_payload.dict()}
        data, status_code = self.__transport.send(
            method=HTTPMethod.GET,
            endpoint=self.__base_url + endpoint,
            params=params
        )
        return data, status_code

    def get_account_types(self, filters: dict = None, offset=0, limit=10,
                          sort_by: str = 'created',
                          sort_order: SortOrder = SortOrder.DESC) -> tuple:
        """
        Get all account types.
        :param filters: A dictionary containing the filters to apply (optional).
        :param offset: Starting point for pagination, default is 0.
        :param limit: The number of account types per page for pagination.
        :param sort_by: The field to sort by, default is 'created'.
        :param sort_order: The order of sorting, default is descending (DESC).
        :return: A list of account types with http status code.
        """
        endpoint = AccountEndpoint.ACCOUNT_TYPES
        params = {**self.__main_payload.dict(), 'offset': offset, 'limit': limit,
                  'sort_by': sort_by, 'sort_order': sort_order}
        if filters and isinstance(filters, dict):
            params.update(filters)
        data, status_code = self.__transport.send(
            method=HTTPMethod.GET,
            endpoint=self.__base_url + endpoint,
            params=params
        )
        return data, status_code

    def get_account_type(self, type_id: str) -> tuple:
        """
        Get specific account type.
        :param type_id: The ID of the account type to retrieve.
        :return: A list of account types with http status code.
        """
        endpoint = AccountTypesEndpoint.ACCOUNT_TYPE.format(type_id=type_id)
        params = {**self.__main_payload.dict()}
        data, status_code = self.__transport.send(
            method=HTTPMethod.GET,
            endpoint=self.__base_url + endpoint,
            params=params
        )
        return data, status_code

