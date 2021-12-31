# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.answer = 0

        def dfs(cur, min_v, max_v):
            if not cur:
                return

            self.answer = max(self.answer, abs(cur.val - min_v), abs(cur.val - max_v))

            min_v = min(cur.val, min_v)
            max_v = max(cur.val, max_v)
            dfs(cur.left, min_v, max_v)
            dfs(cur.right, min_v, max_v)

        dfs(root, root.val, root.val)
        return self.answer
