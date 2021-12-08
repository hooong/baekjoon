# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from leetcode.data_structures.tree_node import TreeNode


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def tilt_dfs(cur):
            left = tilt_dfs(cur.left) if cur.left else 0
            right = tilt_dfs(cur.right) if cur.right else 0

            origin_val = cur.val
            cur.val = abs(left - right)

            return origin_val + left + right

        def sum_dfs(cur):
            left = tilt_dfs(cur.left) if cur.left else 0
            right = tilt_dfs(cur.right) if cur.right else 0
            return cur.val + left + right

        head = root
        tilt_dfs(head)
        head = root
        return sum_dfs(head)
