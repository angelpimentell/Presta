from loans.models.Client import Client
from common.repositories.database_repository import DatabaseRepository


class ClientDatabaseRepository(DatabaseRepository):
    def __init__(self):
        super().__init__(Client)
