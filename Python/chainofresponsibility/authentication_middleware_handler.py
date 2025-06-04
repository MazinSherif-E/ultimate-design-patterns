from requests import Response
from .middleware_handler import MiddlewareHandler

class AuthenticationMiddlewareHandler(MiddlewareHandler):
    def handle(self, request):
        print("Checking if request is authenticated...")
        if not request.is_authenticated:
            print("Request is not authenticated")
            return Response("Authentication Failed", False)
        return super().handle(request)