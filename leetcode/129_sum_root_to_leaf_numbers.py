# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from leetcode.data_structures.tree_node import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs('', root)

    def dfs(self, cur, root):
        cur += str(root.val)

        if root.left and root.right:
            return self.dfs(cur, root.left) + self.dfs(cur, root.right)
        elif root.left:
            return self.dfs(cur, root.left)
        elif root.right:
            return self.dfs(cur, root.right)
        else:
            return int(cur)
