# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        queue.append(root)

        res = []
        depth = 0

        if not root:
            return res

        while queue:
            if len(res) <= depth:
                res.append([])
            
            for _ in range(len(queue)):
                cur = queue.popleft()
                res[depth].append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            depth += 1

        final = []
        for row in res:
            final.append(row[len(row) - 1])

        return final

        
