from .Beverage import Beverage

class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage
    
    def prepare(self) -> str:
        return self.beverage.prepare()