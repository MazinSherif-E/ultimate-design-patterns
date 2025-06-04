from abc import ABC, abstractmethod
from .response import Response

class MiddlewareHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, next_handler):
        """Sets the next middleware in the chain"""
        self.next_handler = next_handler
        return next_handler  # Allows chaining

    @abstractmethod
    def handle(self, request):
        """Processes the request or passes it to the next handler"""
        if self.next_handler:
            return self.next_handler.handle(request)
        return Response("Request has passed all checks successfully", True)
