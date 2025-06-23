from ds_crm_sdk.transports.base import HTTPMethod, AsyncHTTPTransport
from ds_crm_sdk.payloads import MainPayloadBuilder
from .endpoints import AccountEndpoints

# Todo: Return data will be different, work on that next

class AsyncCRMClient:
    def __init__(self, base_url: str, client_type: str, transport: AsyncHTTPTransport, builder: MainPayloadBuilder):
        self.__base_url = base_url
        self.__client_type = client_type
        self.__transport = transport
        self.__builder = builder
        # Creates the main payload based on the client type (skeleton)
        self.__main_payload = self.__builder.build_main_payload(client_type=self.__client_type)

    async def get_account(self, account_id: str):
        """
        Get account details by account ID.
        :param account_id: The ID of the account to retrieve.
        :return: Account details as a dictionary.
        """
        endpoint = AccountEndpoints.SPECIFIC_ACCOUNT.format(account_id=account_id)
        return await self.__transport.send(
            method=HTTPMethod.GET,
            endpoint=self.__base_url + endpoint,
            params=self.__main_payload.dict()
        )

    async def get_accounts_by_filters(self, filters: dict, page=1, page_size=10):
        """
        Get accounts by applying filters.
        :param filters: A dictionary containing the filters to apply.
        :param page: The page number for pagination.
        :param page_size: The number of accounts per page for pagination.
        :return: A list of accounts matching the filters.
        """
        endpoint = AccountEndpoints.BASE
        params = {**self.__main_payload.dict(), **filters, 'page': page, 'page_size': page_size}
        return await self.__transport.send(
            method=HTTPMethod.GET,
            endpoint=self.__base_url + endpoint,
            params=params
        )

    async def get_account_addresses(self, account_id: str, page=1, page_size=10):
        """
        Get addresses for a specific account.
        :param account_id: The ID of the account whose addresses are to be retrieved.
        :param page: The page number for pagination.
        :param page_size: The number of addresses per page for pagination.
        :return: A list of addresses associated with the account.
        """
        endpoint = AccountEndpoints.ACCOUNT_ADDRESSES.format(account_id=account_id)
        params = {**self.__main_payload.dict(), 'page': page, 'page_size': page_size}
        return await self.__transport.send(
            method=HTTPMethod.GET,
            endpoint=self.__base_url + endpoint,
            params=params)

    async def get_account_addresses_by_filters(self, account_id: str, filters: dict, page=1, page_size=10):
        """
        Get addresses for a specific account by applying filters.
        :param account_id: The ID of the account whose addresses are to be retrieved.
        :param filters: A dictionary containing the filters to apply.
        :param page: The page number for pagination.
        :param page_size: The number of addresses per page for pagination.
        :return: A list of addresses associated with the account matching the filters.
        """
        endpoint = AccountEndpoints.ACCOUNT_ADDRESSES.format(account_id=account_id)
        params = {**self.__main_payload.dict(), **filters, 'page': page, 'page_size': page_size}
        return await self.__transport.send(
            method=HTTPMethod.GET,
            endpoint=self.__base_url + endpoint,
            params=params
        )

    async def get_account_types(self, page=1, page_size=10):
        """
        Get all account types.
        :param page: The page number for pagination.
        :param page_size: The number of account types per page for pagination.
        :return: A list of account types.
        """
        endpoint = AccountEndpoints.ACCOUNT_TYPES
        params = {**self.__main_payload.dict(), 'page': page, 'page_size': page_size}
        return await self.__transport.send(
            method=HTTPMethod.GET,
            endpoint=self.__base_url + endpoint,
            params=params
        )
