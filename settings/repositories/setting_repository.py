from settings.models.setting import Setting
from common.repositories.database_repository import DatabaseRepository


class SettingDatabaseRepository(DatabaseRepository):
    def __init__(self):
        super().__init__(Setting)
