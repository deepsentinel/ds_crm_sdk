from pydantic import BaseModel
from typing import Optional


class AccountRequestDTO(BaseModel):
    """
    DTO for building account requests in the CRM system.
    """
    account_type_id: Optional[int] = None
    parent_account_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    phone_number: Optional[str] = None
    email_address: Optional[str] = None
    created_by: str
    user_id: str
    # First name and last name are used to create name and description of the account, so required for now !!!
    first_name: str
    last_name: str
    existing_account_email: Optional[str] = None


