class User:
    def __init__(self, name, chat_mediator):
        self.name = name
        self.chat_mediator = chat_mediator

    def send_direct_message(self, message, to_user):
        self.chat_mediator.send_direct_message(message, to_user, self)

    def receive_direct_message(self, message, from_user):
        print(f"{self.name} is receiving message: '{message}' from user: {from_user.name}")

    def send_group_message(self, message, group_name):
        self.chat_mediator.send_group_message(message, self, group_name)

    def receive_group_message(self, message, from_user, group_name):
        print(f"{self.name} is receiving message: '{message}' from group: '{group_name}' and from user: {from_user.name}")