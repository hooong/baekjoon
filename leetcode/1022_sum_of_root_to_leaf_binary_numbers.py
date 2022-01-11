# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from leetcode.data_structures.tree_node import TreeNode


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(cur, path):
            nonlocal answer

            if not cur:
                return

            path = (path << 1) | cur.val
            if not (cur.left or cur.right):
                answer += path

            dfs(cur.left, path)
            dfs(cur.right, path)

        answer = 0
        dfs(root, 0)
        return answer
