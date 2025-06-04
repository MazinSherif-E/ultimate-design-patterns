from .request import Response
from .middleware_handler import MiddlewareHandler

class SecurityChecksMiddlewareHandler(MiddlewareHandler):
    def handle(self, request):
        print("Checking if request passes security checks...")
        if not request.has_passed_security_checks:
            print("Request failed security checks")
            return Response("Security Check Failed", False)
        return super().handle(request)