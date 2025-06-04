from command import Command

class UnlockDoorCommand(Command):
    def __init__(self, door):
        self.door = door

    def execute(self):
        self.door.unlock()