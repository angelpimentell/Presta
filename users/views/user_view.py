from rest_framework import viewsets
from rest_framework.response import Response

from users.repositories.user_repository import UserDatabaseRepository
from users.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def __init__(self):
        self.user_database_repository = UserDatabaseRepository()

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        user = self.user_database_repository.get_by_id(id=pk)

        serializer = UserSerializer(user)

        return Response(serializer.data)

    def update(self, request, pk=None):
        user = self.user_database_repository.update(id=pk)

        serializer = UserSerializer(user)

        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        user = self.user_database_repository.delete(id=pk)

        serializer = UserSerializer(user)

        return Response(serializer.data)
