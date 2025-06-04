from .MarketingMaterial import MarketingMaterial

class Brochur(MarketingMaterial):
    def __init__(self, layout: str, content: str, color: str):
        super().__init__(layout, content, color)

    def clone(self):
        return Brochur(self.layout, self.content, self.color)

