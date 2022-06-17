from typing import Optional, List, Any


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l: list[Any] = []

        if root is None:
            return l

        stack: list[TreeNode] = [root]

        while stack:
            top: TreeNode = stack.pop()
            l.append(top.val)

            if top.right is not None:
                stack.append(top.right)

            if top.left is not None:
                stack.append(top.left)

        return l




if __name__ == "__main__":
    pass
