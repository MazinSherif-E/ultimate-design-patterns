from CondimentDecorator import CondimentDecorator
from Beverage import Beverage

class MilkDecorator(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)

    def prepare(self) -> str:
        return super().prepare() + " with milk"