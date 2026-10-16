# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        if not root:
            return 0

        count += 1
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if left < right:
            return count + right
        else:
            return count + left



