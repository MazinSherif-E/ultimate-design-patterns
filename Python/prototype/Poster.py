from .MarketingMaterial import MarketingMaterial

class Poster(MarketingMaterial):
    def __init__(self, layout: str, content: str, color: str):
        super().__init__(layout, content, color)

    def clone(self):
        return Poster(self.layout, self.content, self.color)
