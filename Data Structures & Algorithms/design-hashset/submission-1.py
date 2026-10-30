class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next
class MyHashSet:

    def __init__(self):
        self.set = [Node(-1) for _ in range(10000)]

    def hash(self, key):
        return key % len(self.set)

    def add(self, key: int) -> None:
        index = self.hash(key)
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        
        cur.next = Node(key)

    def remove(self, key: int) -> None:
        index = self.hash(key)
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next

        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)