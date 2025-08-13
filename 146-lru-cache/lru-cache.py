class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        #dummy head and tail
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
    #helper functions
    def _remove(self,node):
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node
    def _add_to_head(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
    def _move_to_head(self,node):
        self._remove(node)
        self._add_to_head(node)
    def _pop_tail(self):
        lru_node=self.tail.prev
        self._remove(lru_node)
        return lru_node
        # self.capacity=capacity
        # self.keyvalues={}
        # self.lru={}
        # self.gc=0
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self._move_to_head(node)
        return node.value
        # if key in self.keyvalues:
        #     self.gc+=1
        #     self.lru[key]=self.gc
        #     return self.keyvalues[key]
        # return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self._move_to_head(node)
        else:
            new_node=Node(key,value)
            self.cache[key]=new_node
            self._add_to_head(new_node)
            if len(self.cache)>self.capacity:
                tail_node=self._pop_tail()
                del self.cache[tail_node.key]
        # if key in self.keyvalues:
        #     # Update existing key
        #     self.gc += 1
        #     self.keyvalues[key] = value
        #     self.lru[key] = self.gc
        #     return

        # if len(self.keyvalues) < self.capacity:
        #     self.gc += 1
        #     self.keyvalues[key] = value
        #     self.lru[key] = self.gc
        # else:
        #     least_key = min(self.lru, key=self.lru.get)
        #     del self.keyvalues[least_key]
        #     del self.lru[least_key]       
        #     self.gc += 1
        #     self.keyvalues[key] = value
        #     self.lru[key] = self.gc
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)