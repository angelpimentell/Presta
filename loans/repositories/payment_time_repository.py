from loans.models.payment_time import PaymentTime
from common.repositories.database_repository import DatabaseRepository


class PaymentTimeDatabaseRepository(DatabaseRepository):
    def __init__(self):
        super().__init__(PaymentTime)
