class MyHashMap:

    def __init__(self):
        self.keys = [None] * 1000001
        self.values = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.keys[key] = key
        self.values[key] = value

    def get(self, key: int) -> int:
        if key in self.keys:
            return self.values[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        self.keys[key] = None
        self.values[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)