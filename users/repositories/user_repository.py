from users.models.user import User
from common.repositories.database_repository import DatabaseRepository


class UserDatabaseRepository(DatabaseRepository):
    def __init__(self):
        super().__init__(User)
