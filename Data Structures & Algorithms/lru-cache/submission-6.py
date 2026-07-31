class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.q = collections.deque()

    def get(self, key: int) -> int:
        if key in self.q:  
            self.q.remove(key)
            self.q.append(key)  
            value = self.hashmap.get(key)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.q:
            self.q.remove(key)
        self.q.append(key)
        self.hashmap[key] = value
        if len(self.q) > self.capacity:
            evicted = self.q.popleft() 
            del self.hashmap[evicted]