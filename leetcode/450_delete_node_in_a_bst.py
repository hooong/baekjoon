# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from leetcode.data_structures.tree_node import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        parent = root
        cur = root

        while True:
            if not cur:
                return root
            if cur.val == key:
                break
            elif cur.val < key:
                parent = cur
                cur = cur.right
            else:
                parent = cur
                cur = cur.left

        tmp = None
        if cur.left and cur.right:
            pp = cur.right
            while pp.left:
                pp = pp.left
            pp.left = cur.left
            tmp = cur.right
        elif cur.right:
            tmp = cur.right
        elif cur.left:
            tmp = cur.left

        if cur == root:
            return tmp

        if parent.val < key:
            parent.right = tmp
        else:
            parent.left = tmp

        return root
