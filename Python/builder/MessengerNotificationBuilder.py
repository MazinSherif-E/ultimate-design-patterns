from .NotificationBuilder import NotificationBuilder
from .MessengerNotification import MessengerNotification

class MessengerNotificationBuilder(NotificationBuilder):
    def __init__(self):
        self.content = ""
        self.sender = ""
        self.recipient = ""
        self.time_stamp = ""  
        self.attachments = []
        self.theme = ""
    
    def set_content(self, content: str):
        self.content = content
        return self
    
    def get_content(self):
        return self.content
    
    def set_sender(self, sender: str):
        self.sender = sender
        return self
    
    def get_sender(self):
        return self.sender
    
    def set_recipient(self, recipient: str):
        self.recipient = recipient
        return self
    
    def get_recipient(self):
        return self.recipient
    
    def set_time_stamp(self, time_stamp: str):
        self.time_stamp = time_stamp
        return self
    
    def get_time_stamp(self):
        return self.time_stamp

    def set_attachments(self, attachments: list):
        self.attachments = attachments
        return self
    
    def get_attachments(self):
        return self.attachments

    def set_theme(self, theme: str):
        self.theme = theme
        return self
    
    def get_theme(self):
        return self.theme
    
    def build(self):
        return MessengerNotification(self)