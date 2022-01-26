# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from leetcode.data_structures.tree_node import TreeNode


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(cur):
            if cur is None:
                return []

            tmp = []
            tmp += dfs(cur.left)
            tmp += [cur.val]
            tmp += dfs(cur.right)

            return tmp

        r1 = dfs(root1)
        r2 = dfs(root2)

        answer = []
        while r1 or r2:
            if r1 and r2:
                if r1[0] > r2[0]:
                    answer.append(r2.pop(0))
                else:
                    answer.append(r1.pop(0))
            elif r1:
                answer.append(r1.pop(0))
            elif r2:
                answer.append(r2.pop(0))

        return answer
