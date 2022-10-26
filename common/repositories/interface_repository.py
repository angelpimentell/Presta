from abc import abstractmethod
from abc import ABCMeta


class InterfaceRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_by_id(self, id: int, columns: tuple):
        pass

    @abstractmethod
    def get_by(self, attr: tuple = (), columns: tuple = ()):
        pass

    @abstractmethod
    def list(self, columns: tuple = ()):
        pass

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def update(self, **kwargs):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
