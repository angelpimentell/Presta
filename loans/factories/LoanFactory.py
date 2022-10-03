import factory


class LoanFactory(factory.django.DjangoModelFactory):
    # client = factory.SubFactory(ClientFactory)
    # payment_time = factory.SubFactory(PaymentTimeFactory)
    total_amount = factory.Faker('pydecimal', left_digits=9, right_digits=2, positive=True)
    due_amount = factory.Faker('pydecimal', left_digits=9, right_digits=2, positive=True)
    interests = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    fee_type = factory.Faker('random_int', min=0, max=3)
    start = factory.Faker('date_between')
    finish = factory.Faker('date_between')

    @factory.post_generation
    def clients(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of clients were passed in, use them
            for client in extracted:
                self.clients.add(client)

    class Meta:
        model = "loans.Loan"
