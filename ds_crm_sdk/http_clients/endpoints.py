from enum import Enum

# All CRM endpoints are defined here.


class AccountEndpoints(str, Enum):
    BASE = "/accounts"
    SPECIFIC_ACCOUNT = "/accounts/{account_id}"
    ACCOUNT_ADDRESSES = "/accounts/{account_id}/addresses"
    ACCOUNT_TYPES = "/account_types"


class AccountAddressEndpoints(str, Enum):
    ACCOUNT_ADDRESSES = "/accounts/{account_id}/addresses"


class AccountTypes(str, Enum):
    ACCOUNT_TYPES = "/account_types"

