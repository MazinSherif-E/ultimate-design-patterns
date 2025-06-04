from .ChatManagement import ChatManagement
from .User import User

chat_mediator = ChatManagement()

user1 = User("Alice", chat_mediator)
user2 = User("Bob", chat_mediator)
user3 = User("Charlie", chat_mediator)

chat_mediator.register_user_to_group(user1, "Developers")
chat_mediator.register_user_to_group(user2, "Developers")
chat_mediator.register_user_to_group(user3, "Developers")

user1.send_direct_message("Hey Bob!", user2)
user2.send_group_message("Hello team!", "Developers")