from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    l: Optional[List] = None
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if self.l is None:
            self.l = []
        if root is None:
            return self.l
        if root.left is not None:
            self.inorderTraversal(root.left)
        self.l.append(root.val)
        if root.right is not None:
            self.inorderTraversal(root.right)
        return self.l
