from loans.repositories.payment_repository import PaymentDatabaseRepository
from loans.serializers.laon_serializer import LoanSerializer

from common.views.viewset_extended import ViewSetExtended


class UserViewSet(ViewSetExtended):
    def __init__(self, **kwargs):
        super().__init__(LoanDatabaseRepository, LoanSerializer)
