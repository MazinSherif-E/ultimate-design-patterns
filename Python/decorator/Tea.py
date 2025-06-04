from .Beverage import Beverage

class Tea(Beverage):
    def prepare(self) -> str:
        return "Tea with Tea Leaves"