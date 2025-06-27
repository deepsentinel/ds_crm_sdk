"""
Factories for generating dummy data for testing purposes.
"""
import factory
from faker import Faker
from .dummy_models import DummyAccount

# Initialize Faker instance for generating random data
fake = Faker()


# Note: Each time it fills in the fields with random data
class DummyAccountFactory(factory.Factory):
    class Meta:
        model = DummyAccount

    id = factory.Sequence(lambda n: n + 1)
    name = factory.Faker('company')
    description = factory.Faker('text', max_nb_chars=100)
    email_address = factory.Faker('email')
    phone_number = factory.Faker('phone_number')
    account_type = factory.Faker('random_int', min=1, max=7)
    billing_frequency = factory.Faker('random_int', min=1, max=12)
    is_active = factory.Faker('boolean')
    is_autocollect = factory.Faker('boolean')
    is_vip = factory.Faker('boolean')
    pay_by_check = factory.Faker('boolean')
    external_id = factory.Faker('uuid4')
    stripe_customer_id = factory.Faker('uuid4')
    parent_account = factory.Faker('random_int', min=1, max=7)
    created = factory.LazyFunction(lambda: fake.date_time_this_decade(tzinfo=None).isoformat())
    created_by = factory.Faker('user_name')
    modified = factory.LazyFunction(lambda: fake.date_time_this_decade(tzinfo=None).isoformat())
    modified_by = factory.Faker('user_name')
    last_billing_date = factory.LazyFunction(lambda: fake
                                             .date_time_this_decade(tzinfo=None).isoformat())
