class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.keyvalues={}
        self.lru={}
        self.gc=0
    def get(self, key: int) -> int:
        if key in self.keyvalues:
            self.gc+=1
            self.lru[key]=self.gc
            return self.keyvalues[key]
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.keyvalues:
            # Update existing key
            self.gc += 1
            self.keyvalues[key] = value
            self.lru[key] = self.gc
            return

        if len(self.keyvalues) < self.capacity:
            self.gc += 1
            self.keyvalues[key] = value
            self.lru[key] = self.gc
        else:
            least_key = min(self.lru, key=self.lru.get)
            del self.keyvalues[least_key]
            del self.lru[least_key]       
            self.gc += 1
            self.keyvalues[key] = value
            self.lru[key] = self.gc

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)