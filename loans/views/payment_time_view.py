from loans.repositories.payment_time_repository import PaymentTimeDatabaseRepository
from loans.serializers.payment_serializer import PaymentSerializer

from common.views.viewset_extended import ViewSetExtended


class UserViewSet(ViewSetExtended):
    def __init__(self, **kwargs):
        super().__init__(PaymentTimeDatabaseRepository, PaymentSerializer)
