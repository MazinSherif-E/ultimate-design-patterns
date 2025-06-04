class Light:
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        print(f"Turning on {self.name} light...")

    def turn_off(self):
        print(f"Turning off {self.name} light...")