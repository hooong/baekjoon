# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from leetcode.data_structures.tree_node import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(arr):
            if not arr:
                return None

            mid = len(arr) // 2
            root = TreeNode(val=arr[mid])

            root.left = dfs(arr[:mid])
            root.right = dfs(arr[mid+1:])

            return root

        return dfs(nums)
