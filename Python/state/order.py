class Order:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Order: {self.name}, Price: ${self.price}"
