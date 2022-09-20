import factory

from ..models.Loan import Loan
from ..factories.ClientFactory import ClientFactory
from ..factories.PaymentTimeFactory import PaymentTimeFactory

from faker import Faker

fake = Faker()


class LoanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Loan

    # client = factory.SubFactory(ClientFactory)
    payment_time = factory.SubFactory(PaymentTimeFactory)
    total_amount = fake.pydecimal(left_digits=9, right_digits=2, positive=True)
    due_amount = fake.pydecimal(left_digits=9, right_digits=2, positive=True)
    interests = fake.pydecimal(left_digits=3, right_digits=2, positive=True)
    fee_type = fake.random_int(min=0, max=3)
    start = fake.date_between()
    finish = fake.date_between()

    @factory.post_generation
    def clients(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of clients using bulk addition
        self.clients.add(*extracted)
