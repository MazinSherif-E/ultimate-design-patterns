from command import Command

class LockDoorCommand(Command):
    def __init__(self, door):
        self.door = door

    def execute(self):
        self.door.lock()