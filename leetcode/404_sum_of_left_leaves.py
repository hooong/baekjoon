# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from leetcode.data_structures.tree_node import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)

    def dfs(self, cur, dir=None):
        if cur.left and cur.right:
            return self.dfs(cur.left, 'l') + self.dfs(cur.right, 'r')
        elif cur.left:
            return self.dfs(cur.left, 'l')
        elif cur.right:
            return self.dfs(cur.right, 'r')
        else:
            if dir == 'l':
                return cur.val
            else:
                return 0
