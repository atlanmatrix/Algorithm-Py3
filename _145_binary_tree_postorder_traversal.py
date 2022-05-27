from typing import Optional, List, Any


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l: list = []

        if root is None:
            return []

        stack: list = [root]
        while stack:
            top = stack.pop()
            l.insert(0, top.val)

            if top.left is not None:
                stack.append(top.left)

            if top.right is not None:
                stack.append(top.right)

        return l
