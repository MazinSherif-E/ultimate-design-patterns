from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def get_type(self) -> str:
        pass

