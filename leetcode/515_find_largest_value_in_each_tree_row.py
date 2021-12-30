# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from leetcode.data_structures.tree_node import TreeNode


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        answer = []

        q = [root]
        while q:
            max_value = -(2 ** 31)
            for _ in range(len(q)):
                cur = q.pop(0)
                max_value = max(max_value, cur.val)

                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)
            answer.append(max_value)

        return answer
