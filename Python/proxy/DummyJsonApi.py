from abc import ABC, abstractmethod

class DummyJsonApi(ABC):
    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def get_all_recipes(self):
        pass
