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

        if root.left and root.right:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)

            if left < right:
                print(f"right= {right}, left={left}")
                return count + right
            else:
                print(f"right= {right}, left={left}")
                return count + left
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)

            return left + right + count


