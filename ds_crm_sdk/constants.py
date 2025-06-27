"""All sorts of constants used in the CRM SDK."""
from enum import Enum


class ClientOrigin(str, Enum):
    """
    ClientOrigin Enum to define the origin.
    """
    WEB = "web"
    EWAP = "ewap"
    MOBILE_API = "mobile-api"
    ADMIN_DASHBOARD = "admin-dashboard"


class SortOrder(str, Enum):
    """
    SortOrder Enum to define the sorting order.
    """
    ASC = "ASC"
    DESC = "DESC"
