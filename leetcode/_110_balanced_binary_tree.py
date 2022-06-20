from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        m = {}

        if root is None:
            return True

        def depth(node: Optional[TreeNode]):
            if node is None:
                return 0

            if m.get(id(node.left)) is None:
                m[id(node.left)] = depth(node.left)

            left_depth = m[id(node.left)]

            if m.get(id(node.right)) is None:
                m[id(node.right)] = depth(node.right)

            right_depth = m[id(node.right)]

            return 1 + max(left_depth, right_depth)

        return (abs(depth(root.left) - depth(root.right)) < 2) and self.isBalanced(root.left) and self.isBalanced(root.right)
