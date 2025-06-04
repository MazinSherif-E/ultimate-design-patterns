from http.client import HTTPConnection
from .DummyJsonApi import DummyJsonApi

class DummyThirdPartyService(DummyJsonApi):
    def __init__(self):
        self.connection = HTTPConnection("api.thirdparty.com")

    def get_all_products(self):
        self.connection.request("GET", "/products")
        response = self.connection.getresponse()
        return response.read()
    
    def get_all_recipes(self):
        self.connection.request("GET", "/recipes")
        response = self.connection.getresponse()
        return response.read()
