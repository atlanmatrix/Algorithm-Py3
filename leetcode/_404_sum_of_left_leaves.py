from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum = 0

        if root is None:
            return sum

        node_lst = [(root, 'root')]
        while node_lst:
            node, pos = node_lst.pop(0)
            if pos == 'l' and node.left is None and node.right is None:
                sum += node.val

            if node.left is not None:
                node_lst.append((node.left, 'l'))

            if node.right is not None:
                node_lst.append((node.right, 'r'))

        return sum
