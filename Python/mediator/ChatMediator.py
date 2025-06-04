from abc import ABC, abstractmethod

class ChatMediator(ABC):
    @abstractmethod
    def send_direct_message(self, message, to_user, from_user):
        pass

    @abstractmethod
    def send_group_message(self, message, from_user, to_group):
        pass

    @abstractmethod
    def register_user_to_group(self, user, group_name):
        pass
