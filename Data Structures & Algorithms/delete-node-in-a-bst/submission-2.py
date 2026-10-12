# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Recursion
        if root and key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif root and key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif root and key == root.val:
            if root.left and root.right:
                par = root
                cur = root.right

                while cur.left:
                    par = cur
                    cur = cur.left
                
                root.val = cur.val

                if par.left == cur:
                    par.left = cur.right
                else:
                    par.right = cur.right
            else:
                if root.left:
                    root = root.left
                else:
                    root = root.right
        else:
            return None

        return root
            






        
            