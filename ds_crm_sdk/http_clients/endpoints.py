from enum import Enum

# All CRM endpoints are defined here.


class AccountEndpoint(str, Enum):
    BASE = "/api/crm/accounts"
    SPECIFIC_ACCOUNT = "/api/crm/accounts/{account_id}"
    ACCOUNT_ADDRESSES = "/api/crm/accounts/{account_id}/addresses"
    ACCOUNT_TYPES = "/api/crm/account_types"


class AccountAddressEndpoint(str, Enum):
    ACCOUNT_ADDRESSES = "/api/crm/accounts/{account_id}/addresses"


class AccountTypesEndpoint(str, Enum):
    ACCOUNT_TYPES = "/api/crm/account_types"

