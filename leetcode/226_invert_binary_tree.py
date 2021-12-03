import copy
from typing import Optional

from leetcode.data_structures.tree_node import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(tree):
            if not tree:
                return None

            tree.left, tree.right = dfs(copy.deepcopy(tree.right)), dfs(copy.deepcopy(tree.left))

            return tree

        return dfs(root)
