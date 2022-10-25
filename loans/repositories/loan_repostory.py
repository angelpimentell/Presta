from loans.models.loan import Loan
from common.repositories.database_repository import DatabaseRepository


class LoanDatabaseRepository(DatabaseRepository):
    def __init__(self):
        super().__init__(Loan)
