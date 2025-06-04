from .response import Response

class RequestProcessor:
    def __init__(self, middleware_chain_handler):
        self.middleware_chain_handler = middleware_chain_handler

    def process_request(self, request):
        response = self.middleware_chain_handler.handle(request)
        if not response.success:
            print(response.message)
            return response
        print("Processing request...")
        return Response("Request Successfully Processed", True)