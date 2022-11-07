from loans.repositories.client_repository import ClientDatabaseRepository
from loans.serializers.client_serializer import ClientSerializer

from common.views.viewset_extended import ViewSetExtended


class UserViewSet(ViewSetExtended):
    def __init__(self, **kwargs):
        super().__init__(ClientDatabaseRepository, ClientSerializer)
