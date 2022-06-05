class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.stack = []
    def get(self, key: int) -> int:
        if key in self.d.keys():
            #updating 
            self.stack.remove(key)
            self.stack.append(key)
            return self.d[key]
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key not in self.stack:
            if len(self.stack) == self.capacity:
                del self.d[self.stack[0]]
                self.stack.pop(0)
                self.stack.append(key)
                self.d[key] = value
            else:
                self.stack.append(key)
                self.d[key] = value
        else:
            self.d[key] = value
            self.stack.remove(key)
            self.stack.append(key)
            
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)