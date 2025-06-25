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
    ASC = "ASC"
    DESC = "DESC"
