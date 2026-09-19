# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        while list1:
            arr.append(list1.val)
            list1 = list1.next

        while list2:
            arr.append(list2.val)
            list2 = list2.next

        arr.sort()
        print(arr)

        if not arr:
            return None

        head = ListNode(arr[0])
        curr = head

        i = 1
        while i < len(arr):
            node = ListNode(arr[i])
            curr.next = node
            curr = node
            i += 1

        return head


            

                
