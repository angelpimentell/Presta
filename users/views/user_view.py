from users.repositories.user_repository import UserDatabaseRepository
from users.serializers.user_serializer import UserSerializer

from common.views.viewset_extended import ViewSetExtended


class UserViewSet(ViewSetExtended):
    def __init__(self, **kwargs):
        super().__init__(UserDatabaseRepository, UserSerializer)
