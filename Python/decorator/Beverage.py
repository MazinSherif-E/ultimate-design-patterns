from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def prepare(self) -> str:
        pass