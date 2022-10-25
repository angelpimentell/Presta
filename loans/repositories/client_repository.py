from loans.models.client import Client
from common.repositories.database_repository import DatabaseRepository


class ClientDatabaseRepository(DatabaseRepository):
    def __init__(self):
        super().__init__(Client)
