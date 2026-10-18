# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        def height(root):
            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)

            if left == -1 or right == -1:
                return -1
            if right - left > 1 or right - left < -1 :
                return -1
            else:
                return 1 + max(left, right)

        left = height(root.left)
        print(f"left= {left}")
        right = height(root.right)
        print(f"right= {right}")

        if left == -1 or right == -1:
            return False
        elif right - left > 1 or right - left < -1 :
            return False
        else:
            return True

        







        




                
            

            



            
