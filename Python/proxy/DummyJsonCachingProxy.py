from .DummyJsonApi import DummyJsonApi
from .DummyThirdPartyApiService import DummyThirdPartyService

class DummyJsonCachingProxy(DummyJsonApi):
    def __init__(self):
        self.dummyThirdPartyService = DummyThirdPartyService()
        self.caching_layer = {}

    def get_all_products(self):
        if "products" in self.caching_layer:
            return self.caching_layer["products"]
        self.caching_layer["products"] = self.dummyThirdPartyService.get_all_products()
        return self.caching_layer["products"]

    def get_all_recipes(self):
        if "recipes" in self.caching_layer:
            return self.caching_layer["recipes"]
        self.caching_layer["recipes"] = self.dummyThirdPartyService.get_all_recipes()
        return self.caching_layer["recipes"]

