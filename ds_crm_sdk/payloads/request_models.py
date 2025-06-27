"""
DS CRM SDK Request Payloads
"""
from pydantic import BaseModel
from ds_crm_sdk.constants import SortOrder


class RequestPayloadBase(BaseModel):
    """
    Base class for all request payloads in the DS CRM SDK.
    """
    filters: dict = {}
    sort_by: str = None
    sort_order: SortOrder = None
    offset: int = None
    limit: int = None


class WebPayloadBase(RequestPayloadBase):
    """
    Base class for web client request payloads in the DS CRM SDK.
    """
    client_origin: str = 'web'


class EWAPPayloadBase(RequestPayloadBase):
    """
    Base class for EWAP client request payloads in the DS CRM SDK.
    """
    client_origin: str = 'ewap'


class MobileAPIPayloadBase(RequestPayloadBase):
    """
    Base class for mobile API request payloads in the DS CRM SDK.
    """
    client_origin: str = 'mobile-api'


class AdminDashboardPayloadBase(RequestPayloadBase):
    """
    Base class for admin dashboard request payloads in the DS CRM SDK.
    """
    client_origin: str = 'admin-dashboard'


