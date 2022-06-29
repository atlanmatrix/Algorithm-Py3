from typing import Optional

from data_struct.tree import to_binary_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value = root.val

        def dfs(node):
            if node is None:
                return True

            return node.val == value and dfs(node.left) and dfs(node.right)

        return dfs(root)


if __name__ == "__main__":
    s = Solution()
    print(s.isUnivalTree(to_binary_tree([1, 1, 1, 1, 2, None, 1])))
