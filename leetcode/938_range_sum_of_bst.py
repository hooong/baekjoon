# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from leetcode.data_structures.tree_node import TreeNode


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(cur):
            if not cur:
                return 0

            if low <= cur.val <= high:
                return dfs(cur.left) + dfs(cur.right) + cur.val
            elif cur.val < low:
                return dfs(cur.right)
            elif high < cur.val:
                return dfs(cur.left)
            else:
                return 0

        return dfs(root)
