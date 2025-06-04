from .DummyJsonCachingProxy import DummyJsonCachingProxy

dummyJsonCachingProxy = DummyJsonCachingProxy()

print(dummyJsonCachingProxy.get_all_products())
print(dummyJsonCachingProxy.get_all_recipes())

