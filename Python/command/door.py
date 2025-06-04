class Door:
    def __init__(self, name):
        self.name = name

    def lock(self):
        print(f"Locking {self.name} door...")

    def unlock(self):
        print(f"Unlocking {self.name} door...")