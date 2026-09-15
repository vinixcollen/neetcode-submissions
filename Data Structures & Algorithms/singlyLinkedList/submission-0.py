class Node:
    def __init__(self, val):
        self.val = val
        self.next: Node | None = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        count = 0
        current = self.head
        if index == 0:
            if not current:
                return -1
            else:
                return current.val
        else:
            while count < index:
                if not current:
                    return -1
                else:
                    current = current.next
                    count += 1
                
            if not current:
                return -1
                
            return current.val

    def insertHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head
        self.head = new
            
    def insertTail(self, val: int) -> None:
        tail = Node(val)
        if self.head is not None:
            if self.head.next == None:
                self.head.next = tail
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = tail
        else:
            self.head = tail
    
    def remove(self, index: int) -> bool:
        count = 0
        current = self.head
        if index == 0:
            if current is None:
                return False
            else:
                self.head = current.next
                return True
        else:
            while count < index:
                if not current: 
                    return False
                else:
                    if count == index - 1:
                        if current.next is None:
                            return False
                        else:
                            current.next = current.next.next
                            return True
                    else:
                        current = current.next
                        count += 1

            return True
            
    def getValues(self) -> List[int]:
        ll = []
        current = self.head

        if current:
            ll.append(current.val)
            while current.next != None:
                current = current.next
                ll.append(current.val)
            return ll
        else:
            return ll

            
        

