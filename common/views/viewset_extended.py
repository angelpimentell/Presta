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

    def __init__(self, **kwargs):
        self.user_database_repository = UserDatabaseRepository()

    def list(self, request):
        queryset = self.user_database_repository.list()

        serializer = UserSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request):
        user = self.user_database_repository.create(**request.data[0])

        serializer = UserSerializer(user)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.user_database_repository.get_by_id(id=pk)

        serializer = UserSerializer(queryset, many=True)

        return Response(serializer.data)

    def update(self, request, pk=None):
        user = self.user_database_repository.update(id=pk, **request.data[0])

        serializer = UserSerializer(user)

        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        self.user_database_repository.delete(id=pk)

        return Response(pk)
