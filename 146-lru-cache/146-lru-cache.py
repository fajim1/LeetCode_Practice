class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.capacity = capacity
        self.lru = []

    def get(self, key: int) -> int:
        
        
        if key in self.dic.keys():
            
            if key in self.lru:
                self.lru.remove(key)
                
                self.lru.append(key)
            else:
                self.lru.append(key)
            
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if self.capacity != 0 and key not in self.dic.keys():
            self.dic[key] = value
            self.capacity = self.capacity - 1
            
            if key in self.lru:
                self.lru.remove(key)
                
                self.lru.append(key)
            
            else:
                self.lru.append(key)
        
        elif self.capacity == 0 and key not in self.dic.keys():
            
            self.dic.pop(self.lru[0])
            self.lru.pop(0)
            
            self.dic[key] = value
            
            self.lru.append(key)
                
        
            
        else:
            
            self.dic[key] = value
            
            if key in self.lru:
                self.lru.remove(key)
                
                self.lru.append(key)
            
            else:
                self.lru.append(key)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)