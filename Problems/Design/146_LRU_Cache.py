"""
Runtime: 188 ms, faster than 75.16% of Python3 online submissions for LRU Cache.
Memory Usage: 23 MB, less than 6.06% of Python3 online submissions for LRU Cache.
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
                    
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)