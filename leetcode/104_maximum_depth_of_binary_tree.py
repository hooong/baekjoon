from typing import Optional

from leetcode.data_structures.tree_node import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        cnt = self.check_depth(root, 1)
        return cnt

    def check_depth(self, node, cnt):
        if node.left and node.right:
            return max(self.check_depth(node.left, cnt + 1), self.check_depth(node.right, cnt + 1))
        if node.left:
            return self.check_depth(node.left, cnt + 1)
        elif node.right:
            return self.check_depth(node.right, cnt + 1)
        else:
            return cnt
