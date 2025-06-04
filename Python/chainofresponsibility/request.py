class Request:
    def __init__(self, request_type, is_authenticated, is_authorized, has_passed_security_checks):
        self.request_type = request_type
        self.is_authenticated = is_authenticated
        self.is_authorized = is_authorized
        self.has_passed_security_checks = has_passed_security_checks
