from .request import Request
from .authentication_middleware_handler import AuthenticationMiddlewareHandler
from .authorization_middleware_handler import AuthorizationMiddlewareHandler
from .request_processor import RequestProcessor
from .security_check_middleware_handler import SecurityChecksMiddlewareHandler


if __name__ == "__main__":
    # Create middleware chain
    auth_handler = AuthenticationMiddlewareHandler()
    authz_handler = AuthorizationMiddlewareHandler()
    security_handler = SecurityChecksMiddlewareHandler()

    # Set up the chain: Authentication -> Authorization -> Security
    auth_handler.set_next(authz_handler).set_next(security_handler)

    # Create a processor with the middleware chain
    processor = RequestProcessor(auth_handler)

    # Create a test request
    request = Request("API_CALL", is_authenticated=True, is_authorized=True, has_passed_security_checks=True)

    # Process the request
    response = processor.process_request(request)
    print(f"Final Response: {response.message}, Success: {response.success}")
