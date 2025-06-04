class SmartHomeShortcut:
    def __init__(self):
        self.commands = {}

    def set_command(self, shortcut_command, command):
        self.commands[shortcut_command] = command

    def open_shortcut(self, shortcut_command):
        if shortcut_command in self.commands:
            self.commands[shortcut_command].execute()
        else:
            print(f"No command assigned for: {shortcut_command}")