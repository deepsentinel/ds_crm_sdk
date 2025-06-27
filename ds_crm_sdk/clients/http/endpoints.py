"""
Endpoints for CRM Account Management
"""
from enum import Enum


class AccountEndpoint(str, Enum):
    """
    Endpoints for managing CRM accounts.
    """
    BASE = "/api/crm/accounts"
    SPECIFIC_ACCOUNT = "/api/crm/accounts/{account_id}"
    ACCOUNT_TYPES = "/api/crm/account_types"


class AccountAddressEndpoint(str, Enum):
    """
    Endpoints for managing account addresses.
    """
    ACCOUNT_ADDRESSES = "/api/crm/accounts/{account_id}/addresses"
    ACCOUNT_ADDRESS = "/api/crm/accounts/{account_id}/addresses/{address_id}"


class AccountTypesEndpoint(str, Enum):
    """
    Endpoints for managing account types.
    """
    ACCOUNT_TYPES = "/api/crm/account_types"
    ACCOUNT_TYPE = "/api/crm/account_types/{type_id}"


