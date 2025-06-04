from abc import ABC, abstractmethod

class MarketingMaterial(ABC):
    def __init__(self, layout: str, content: str, color: str):
        self.layout = layout
        self.content = content
        self.color = color

    def get_layout(self):
        return self.layout

    def get_content(self):
        return self.content

    def get_color(self):
        return self.color
    
    def set_layout(self, layout: str):
        self.layout = layout

    def set_content(self, content: str):
        self.content = content

    def set_color(self, color: str):
        self.color = color
    
    def print_info(self):
        print(f"Layout: {self.layout}, Content: {self.content}, Color: {self.color}")

    @abstractmethod
    def clone(self):
        pass
