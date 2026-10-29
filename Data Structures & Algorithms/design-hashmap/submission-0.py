class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        if len(self.hashmap) <= key:
            needed_slot = (key + 1) - len(self.hashmap)
            self.hashmap.extend([None] * needed_slot)
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        if key < len(self.hashmap) and self.hashmap[key] is not None:
            return self.hashmap[key]
        return -1

    def remove(self, key: int) -> None:
        if key < len(self.hashmap) and self.hashmap[key] is not None:
            self.hashmap[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)