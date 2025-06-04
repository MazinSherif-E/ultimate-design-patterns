from .Beverage import Beverage

class Coffee(Beverage):
    def prepare(self) -> str:
        return "Coffee with Coffee Beans"