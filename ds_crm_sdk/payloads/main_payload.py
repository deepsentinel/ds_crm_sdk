from pydantic import BaseModel


class WebPayloadBase(BaseModel):
    client_origin: str = 'web'


class EwapPayloadBase(BaseModel):
    client_origin: str = 'ewap'


class MobileAPIPayloadBase(BaseModel):
    client_origin: str = 'mobile-api'


class AdminDashboardPayloadBase(BaseModel):
    client_origin: str = 'admin-dashboard'


