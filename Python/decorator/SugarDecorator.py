from .Beverage import Beverage
from .CondimentDecorator import CondimentDecorator

class SugarDecorator(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)
    
    def prepare(self) -> str:
        return super().prepare() + " with sugar"