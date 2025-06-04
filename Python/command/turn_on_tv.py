from .command import Command

class TurnOnTV(Command):
    def __init__(self, tv):
        self.tv = tv
    def execute(self):
        self.tv.turn_on()