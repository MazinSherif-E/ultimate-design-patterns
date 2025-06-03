from abc import ABC, abstractmethod

class OrderState(ABC):
    """Abstract base class for all order states."""
    
    @abstractmethod
    def process_order(self):
        pass
    
    @abstractmethod
    def ship_order(self):
        pass
    
    @abstractmethod
    def deliver_order(self):
        pass
    
    @abstractmethod
    def cancel_order(self):
        pass
