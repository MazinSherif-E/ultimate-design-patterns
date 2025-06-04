from .Player import Player
from .Weapon import Weapon

class WeakEnemy(Player):
    def __init__(self, display_name: str = "Enemy", health_bar: int = 5, attack_power: int = 1, weapon: Weapon = None):
        self.display_name = display_name
        self.health_bar = health_bar
        self.attack_power = attack_power
        self.weapon = weapon

    def attack(self):
        print(f"Weak {self.display_name} is attacking with {self.weapon.name} and {self.weapon.ponus_attack} damage")
