from .response import Response
from .middleware_handler import MiddlewareHandler

class AuthorizationMiddlewareHandler(MiddlewareHandler):
    def handle(self, request):
        print("Checking if request is authorized...")
        if not request.is_authorized:
            print("Request failed to be authorized")
            return Response("Authorization Failed", False)
        return super().handle(request)