"""
This module contains dummy data models for testing purposes.
"""
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class DummyAccount:
    id: int = 10
    name: str = "NA"
    description: str = "NA"
    email_address: str = "NA"
    phone_number: str = "6505559004"
    account_type: int = 7
    billing_frequency: int = 3
    is_active: bool = True
    is_autocollect: bool = True
    is_vip: bool = True
    pay_by_check: bool = False
    external_id: Optional[str] = None
    stripe_customer_id: str = "cus_cloud123"
    parent_account: int = 7
    created: str = "Thu, 19 Jun 2025 07:53:22 GMT"
    created_by: str = "system"
    modified: str = "Thu, 19 Jun 2025 07:53:22 GMT"
    modified_by: str = "system"
    last_billing_date: str = "Sun, 01 Jun 2025 00:00:00 GMT"

    def to_dict(self):
        """
        Convert the DummyAccount instance to a dictionary representation.
        :return:
        """
        return asdict(self)


@dataclass
class DummyAccountType:
    commission_rate: int = 0
    created: str = "Thu, 19 Jun 2025 07:53:07 GMT"
    description: str = "Internal Deep Sentinel account"
    id: int = 1
    is_partner: bool = False
    modified: str = "Thu, 19 Jun 2025 07:53:07 GMT"
    name: str = "Deep Sentinel"

    def to_dict(self):
        """
        Convert the AccountType instance to a dictionary representation.
        :return:
        """
        return asdict(self)
