# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        left_result = self.inorderTraversal(root.left)
        right_result = self.inorderTraversal(root.right)  
        
        return left_result + [root.val] + right_result


        

                
        
        

        

        

            
