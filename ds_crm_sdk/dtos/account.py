from pydantic import BaseModel


class AccountRequestDTO(BaseModel):
    """
    DTO for building account requests in the CRM system.
    """
    account_type_id: int
    parent_account_id: int
    name: str = None
    phone_number: str = None
    email_address: str = None
    created_by: str = None
    # This field is used to associate the account with a user in the system (account_user)
    user_id: str = None
    # This field is used to check if the account already exists, if it does, then this is just an association request,
    # no new account will be created.
    existing_account_email: str = None
