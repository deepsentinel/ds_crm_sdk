from pydantic import BaseModel


class WebPayloadBase(BaseModel):
    client_type: str = 'web'


class EwapPayloadBase(BaseModel):
    client_type: str = 'ewap'


class MobileAPIPayloadBase(BaseModel):
    client_type: str = 'mobile-api'


class AdminDashboardPayloadBase(BaseModel):
    client_type: str = 'admin-dashboard'


