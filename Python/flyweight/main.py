from .MainPlayer import MainPlayer
from .WeakEnemy import WeakEnemy
from .StrongEnemy import StrongEnemy
from .Weapon import Weapon

main_player = MainPlayer(weapon=Weapon("Sword", 10))
weak_enemy = WeakEnemy(weapon=Weapon("Knife", 5))
strong_enemy = StrongEnemy(weapon=Weapon("Sword", 10))

main_player.attack()
weak_enemy.attack()
strong_enemy.attack()