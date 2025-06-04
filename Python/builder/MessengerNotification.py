from .MessengerNotificationBuilder import MessengerNotificationBuilder

class MessengerNotification:
    def __init__(self, builder: MessengerNotificationBuilder):
        self._content = builder.get_content()
        self._sender = builder.get_sender()
        self._recipient = builder.get_recipient()
        self._time_stamp = builder.get_time_stamp()
        self._attachments = builder.get_attachments()
        self._theme = builder.get_theme()
    
    def get_content(self):
        return self._content
    
    def get_sender(self):
        return self._sender
    
    def get_recipient(self):
        return self._recipient
    
    def get_time_stamp(self):
        return self._time_stamp
    
    def get_attachments(self):
        return self._attachments
    
    def get_theme(self):
        return self._theme
