from .ChatMediator import ChatMediator

class ChatManagement(ChatMediator):
    def __init__(self):
        self.groups = {}

    def send_direct_message(self, message, to_user, from_user):
        print(f"{from_user.name} is sending message: '{message}' to user: {to_user.name}")
        to_user.receive_direct_message(message, from_user)

    def send_group_message(self, message, from_user, to_group):
        print(f"{from_user.name} is sending message: '{message}' to group: '{to_group}'")
        users = self.groups.get(to_group, [])
        for user in users:
            if user != from_user:
                user.receive_group_message(message, from_user, to_group)

    def register_user_to_group(self, user, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = []
        self.groups[group_name].append(user)
