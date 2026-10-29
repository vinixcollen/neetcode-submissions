# Linked List Solution

class Node:
    def __init__(self, key, val, next=None):
        self.key, self.val = key, val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.map = [None] * 10

    def hash(self, key):
        return key % 10

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        if not self.map[index]:
            self.map[index] = Node(key, value)
        else:
            cur = self.map[self.hash(key)]
            while cur:
                if cur.key == key:
                    cur.val = value
                    return

                if cur.next is None:
                    cur.next = Node(key, value)
                    return
                
                cur = cur.next
        
    def get(self, key: int) -> int:
        if self.map[self.hash(key)]:
            cur = self.map[self.hash(key)]
            while cur:
                if cur.key == key:
                    return cur.val
                cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        cur = self.map[index]

        if cur and cur.key == key:
            self.map[index] = cur.next
            return

        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)