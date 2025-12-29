from collections import OrderedDict
class LRUCache:
   def __init__(self,cap):
      self.cap=cap
      self.cache=OrderedDict()
   def get(self,key):
      if key not in self.cache:
         return -1
      self.cache.move_to_end(key)
      return self.cache[key]
   def put(self,key, val):
      if key in self.cache:
         self.cache.move_to_end(key)
         self.cache[key]=val
      else:self.cache[key]=val
      if len(self.cache)>self.cap:
         self.cache.popitem(last=False)
cache = LRUCache(3) #capacity 3, creating instance

cache.put(1, 'A')
cache.put(2, 'B')
cache.put(3, 'C')

print(cache.get(1)) #A
print(cache.get(2))

cache.put(4, 'D')
print(list(cache.cache.items())) #key 3 was evicted because lru