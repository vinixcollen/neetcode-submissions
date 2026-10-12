# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        prev = None
        curr = root
        while curr and curr.val != key:
            prev = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        
        # key not found
        if curr is None:
            return root
        
        # two child
        if curr.left and curr.right:
            successor_parent = curr
            # left subtree
            successor = curr.left

            # find the largest number in the left subtree
            while successor.right:
                successor_parent = successor
                successor = successor.right

            #Replace value 
            curr.val = successor.val

            #delete the successor node as it has replaced the deleted nodes above
            if successor_parent.right == successor:
                successor_parent.right = successor.left
            else:
                successor_parent.left = successor.left
        # one or none child
        else:
            if curr.left:
                child = curr.left
            else:
                child = curr.right

            if prev is None:
                return child
            
            if prev.left == curr:
                prev.left = child
            else:
                prev.right = child
            
        return root
            






        
            