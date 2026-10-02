# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def divide(lists):
            mid = len(lists) // 2
            left = lists[:mid]
            right = lists[mid:]

            if len(lists) == 2:
                return merge(lists[0], lists[1])
            elif len(lists) <= 1:
                return lists[0]
            
            left = divide(left)
            right = divide(right)

            return merge(left, right)
            
        def merge(left, right):
            new_head = ListNode()
            curr = new_head
            
            while left and right:
                if left.val <= right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next

            if left:
                curr.next = left
            else:
                curr.next = right
            
            return new_head.next

        if lists:
            return divide(lists)
        else:
            return None






