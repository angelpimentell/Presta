from rest_framework import viewsets
from rest_framework.response import Response


class ViewSetExtended(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def __init__(self, repository=None, serializer=None):
        self.repository = repository()
        self.serializer = serializer

    def list(self, request):
        queryset = self.repository.list()

        serializer = self.serializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request):
        user = self.repository.create(**request.data[0])

        serializer = self.serializer(user)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.repository.get_by_id(id=pk)

        serializer = self.serializer(queryset, many=True)

        return Response(serializer.data)

    def update(self, request, pk=None):
        user = self.repository.update(id=pk, **request.data[0])

        serializer = self.serializer(user)

        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        self.repository.delete(id=pk)

        return Response(pk)
