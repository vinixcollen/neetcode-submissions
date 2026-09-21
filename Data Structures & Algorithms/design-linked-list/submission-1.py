class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)

    def get(self, index: int) -> int:
        curr = self.head
        if curr.next is None:
            return -1
        else:
            i = 0
            curr = self.head.next
            while curr:
                if i == index:
                    return curr.val
                curr = curr.next
                i += 1

            return -1

    def addAtHead(self, val: int) -> None:
            new_head = Node(val)

            if self.head.next:
                new_head.next = self.head.next
                self.head.next.prev = new_head
                self.head.next = new_head
            else:
                self.head.next = new_head
            new_head.prev = self.head

    def addAtTail(self, val: int) -> None:
        tail = self.head
        if tail.next is None:
            tail.next = Node(val)
            tail = tail.next
            tail.prev = self.head
        else:
            while tail.next is not None:
                tail = tail.next
            tail.next = Node(val)
            tail.next.prev = tail
            tail = tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        len = 0
        curr = self.head
        while curr.next is not None:
            curr = curr.next
            len += 1

        if index == 0:
            self.addAtHead(val)
        elif index == len:
            self.addAtTail(val)
        elif index > len:
            return None
        else:
            i = 0
            curr = self.head.next
            while curr is not None:
                if i == index:
                    new_node = Node(val)
                    new_node.next = curr
                    new_node.prev = curr.prev
                    curr.prev.next = new_node
                    curr.prev = new_node
                    return
                curr = curr.next
                i += 1
      
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                return
            curr = curr.next
            i += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)