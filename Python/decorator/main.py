from Coffee import Coffee
from SugarDecorator import SugarDecorator
from MintDecorator import MintDecorator

coffee = Coffee()
coffee_with_sugar = SugarDecorator(coffee)
coffee_with_sugar_and_mint = MintDecorator(coffee_with_sugar)
print(coffee_with_sugar_and_mint.prepare())  # Output: Coffee with Coffee Beans with sugar with Mint