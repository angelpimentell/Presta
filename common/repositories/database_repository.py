from common.repositories.interface_repository import InterfaceRepository


class DatabaseRepository(InterfaceRepository):
    def __init__(self, model):
        self.model = model

    def get_by_id(self, id: int, columns: tuple = ()):
        return self.model.objects.filter(id=id).values(*columns)

    def get_by(self, columns: tuple = (), **kwargs):
        return self.model.objects.filter(**kwargs).values(*columns)

    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def update(self, **kwargs):
        # TODO: Find way to raise ObjectDoesNotExist when filter count is 0
        self.model.objects.filter(pk=kwargs['id']).update(**kwargs)
        return kwargs['id']

    def delete(self, id: int):
        return self.model.objects.filter(id=id).delete()
