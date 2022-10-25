from loans.models.payment import Payment
from common.repositories.database_repository import DatabaseRepository


class PaymentDatabaseRepository(DatabaseRepository):
    def __init__(self):
        super().__init__(Payment)
