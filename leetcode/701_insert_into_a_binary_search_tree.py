# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from leetcode.data_structures.tree_node import TreeNode


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def dfs(cur):
            if not cur:
                return TreeNode(val)

            if val < cur.val:
                cur.left = dfs(cur.left)
            else:
                cur.right = dfs(cur.right)
            return cur

        head = root
        dfs(head)
        return root
