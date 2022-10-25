from users.models.User import User
from common.repositories.database_repository import DatabaseRepository


class UserRepository(DatabaseRepository):
    def __init__(self):
        super().__init__(User)
