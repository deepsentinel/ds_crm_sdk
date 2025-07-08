"""
Sync CRMClient for interacting with CRM API endpoints.
"""
# pylint: disable=duplicate-code
from ds_crm_sdk.transports.http.base import HTTPMethod, HTTPTransport
from ds_crm_sdk.payloads import MainPayloadBuilder
from ds_crm_sdk.constants import ClientOrigin, SortOrder
from .endpoints import AccountEndpoint, AccountAddressEndpoint, AccountTypesEndpoint
from .base import BaseCRMClient
from ds_crm_sdk.sdk_contracts import CRMClientAPI
from ...dtos import AccountRequestDTO


class CRMClient(BaseCRMClient, CRMClientAPI):
    """
    Synchronous CRMClient for interacting with CRM API endpoints.
    """
    def __init__(self, base_url: str, client_origin: ClientOrigin,
                 transport: HTTPTransport):
        super().__init__(base_url=base_url, builder=MainPayloadBuilder(client_origin=client_origin))
        self.__transport = transport

    def get_account(self, account_id: str) -> tuple:
        """
        Get account details by account ID.
        :param account_id: The ID of the account to retrieve.
        :return: Account details as a dictionary with http status code.
        """
        endpoint = self._build_endpoint_url(endpoint_template=AccountEndpoint.SPECIFIC_ACCOUNT,
                                            values_to_inject={'account_id': account_id})
        params = self._builder.build_main_payload()
        data, status_code = self.__transport.send(
            method=HTTPMethod.GET,
            endpoint=endpoint,
            params=params
        )
        return data, status_code

    def get_accounts(self, filters: dict = None, offset=0, limit=10,
                     sort_by: str = 'name', sort_order: SortOrder = SortOrder.DESC) -> tuple:
        """
        Get accounts with filters.
        :param filters: A dictionary containing the filters to apply (optional).
        :param offset: Starting point for pagination, default is 0.
        :param limit: The number of accounts per page for pagination.
        :param sort_by: The field to sort by, default is 'created'.
        :param sort_order: The order of sorting, default is descending (DESC).
        :return: A list of accounts matching the filters with http status code
        """
        endpoint = self._build_endpoint_url(endpoint_template=AccountEndpoint.ACCOUNTS)
        params = self._builder.build_main_payload(**{'offset': offset, 'limit': limit,
                                                     'sort_by': sort_by, 'sort_order': sort_order,
                                                     'filters': filters})
        data, status_code = self.__transport.send(
            method=HTTPMethod.GET,
            endpoint=endpoint,
            params=params
        )
        return data, status_code

    def get_account_addresses(self, account_id: str, filters: dict = None, offset=0, limit=10,
                              sort_by: str = 'created',
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
        endpoint = self._build_endpoint_url(endpoint_template=AccountAddressEndpoint.ACCOUNT_ADDRESSES,
                                            values_to_inject={'account_id': account_id})
        params = self._builder.build_main_payload(**{'offset': offset, 'limit': limit,
                                                     'sort_by': sort_by, 'sort_order': sort_order,
                                                     'filters': filters})
        data, status_code = self.__transport.send(
            method=HTTPMethod.GET,
            endpoint=endpoint,
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
        endpoint = self._build_endpoint_url(endpoint_template=AccountAddressEndpoint.ACCOUNT_ADDRESS,
                                            values_to_inject={'account_id': account_id,
                                                              'address_id': address_id})
        params = self._builder.build_main_payload()
        data, status_code = self.__transport.send(
            method=HTTPMethod.GET,
            endpoint=endpoint,
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
        endpoint = self._build_endpoint_url(AccountEndpoint.ACCOUNT_TYPES)
        params = self._builder.build_main_payload(**{'offset': offset, 'limit': limit,
                                                     'sort_by': sort_by, 'sort_order': sort_order,
                                                     'filters': filters})
        data, status_code = self.__transport.send(
            method=HTTPMethod.GET,
            endpoint=endpoint,
            params=params
        )
        return data, status_code

    def get_account_type(self, type_id: str) -> tuple:
        """
        Get specific account type.
        :param type_id: The ID of the account type to retrieve.
        :return: A list of account types with http status code.
        """
        endpoint = self._build_endpoint_url(endpoint_template=AccountTypesEndpoint.ACCOUNT_TYPE,
                                            values_to_inject={'type_id': type_id})
        params = self._builder.build_main_payload()
        data, status_code = self.__transport.send(
            method=HTTPMethod.GET,
            endpoint=endpoint,
            params=params
        )
        return data, status_code

    def create_account(self, account_data: AccountRequestDTO) -> tuple:
        """
        Create a new account.
        :param account_data: An instance of AccountRequestDTO containing the account details.
        :return: The created account details with http status code.
        """
        endpoint = self._build_endpoint_url(AccountEndpoint.ACCOUNTS)
        params = self._builder.build_main_payload()
        complete_data = params.update({**account_data.model_dump(exclude_none=True)})
        data, status_code = self.__transport.send(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            payload=complete_data
        )
        return data, status_code

