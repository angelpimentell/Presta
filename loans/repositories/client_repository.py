from loans.models.client import Client
from common.repositories.database_repository import DatabaseRepository


# TODO: Specify that onlye you can import the ClientDatabaseRepository
class ClientDatabaseRepository(DatabaseRepository):
    def __init__(self):
        super().__init__(Client)
