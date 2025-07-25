from abc import ABC, abstractmethod


class AsyncCRMClientAPI(ABC):
    """
    Defines the interface for interacting with CRM API endpoints.
    """

    @abstractmethod
    async def get_account(self, account_id: str) -> tuple:
        """
        Get account details by account ID.
        :param account_id: The ID of the account to retrieve.
        :return: Account details as a dictionary with http status code.
        """
        ...

    @abstractmethod
    async def get_accounts(self, filters: dict = None, offset=0, limit=10,
                           sort_by: str = 'name', sort_order: str = 'DESC') -> tuple:
        """
        Get accounts with filters.
        :param filters: A dictionary containing the filters to apply (optional).
        :param offset: Starting point for pagination, default is 0.
        :param limit: The number of accounts per page for pagination.
        :param sort_by: The field to sort by, default is 'created'.
        :param sort_order: The order of sorting, default is descending (DESC).
        :return: A list of accounts matching the filters with http status code
        """
        ...

    @abstractmethod
    async def get_account_addresses(self, account_id: str, filters: dict = None, offset=0, limit=10,
                                    sort_by: str = 'created',
                                    sort_order: str = 'DESC') -> tuple:
        """
        Get addresses for a specific account.
        :param account_id: The ID of the account whose addresses are to be retrieved.
        :param filters: A dictionary containing the filters to apply (optional).
        :param offset: Starting point for pagination, default is 0.
        :param limit: The number of addresses per page for pagination.
        :param sort_by: The field to sort by, default is 'address.created'.
        :param sort_order: The order of sorting, default is descending (DESC).
        :return: A list of addresses for the specified account with http status code
        """
        ...

    @abstractmethod
    async def get_account_address(self, account_id: str, address_id: str) -> tuple:
        """
        Get a specific address for a specific account.
        :param account_id: The ID of the account whose address is to be retrieved.
        :param address_id: The ID of the address to retrieve.
        :return: Address details with http status code.
        """
        ...

    @abstractmethod
    async def get_account_types(self, filters: dict = None, offset=0, limit=10,
                                sort_by: str = 'created',
                                sort_order: str = 'DESC') -> tuple:
        """
        Get all account types.
        :param filters: A dictionary containing the filters to apply (optional).
        :param offset: Starting point for pagination, default is 0.
        :param limit: The number of account types per page for pagination.
        :param sort_by: The field to sort by, default is 'created'.
        :param sort_order: The order of sorting, default is descending (DESC).
        :return: A list of account types with http status code.
        """
        ...

    @abstractmethod
    async def get_account_type(self, type_id: str) -> tuple:
        """
        Get specific account type.
        :param type_id: The ID of the account type to retrieve.
        :return: Account type details with http status code.
        """
        ...

