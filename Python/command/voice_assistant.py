class VoiceAssistant:
    def __init__(self):
        self.commands = {}

    def set_command(self, talking_command, command):
        self.commands[talking_command] = command

    def say(self, talking_command):
        if talking_command in self.commands:
            self.commands[talking_command].execute()
        else:
            print(f"No command found for: {talking_command}")