from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None:
            if root2 is None:
                return True
            else:
                return False
        else:
            if root2 is None:
                return False

        leaves = []
        node_lst: list[TreeNode] = [root1]

        while node_lst:
            node = node_lst.pop()
            if node.left is None and node.right is None:
                leaves.append(node.val)

            if node.right is not None:
                node_lst.append(node.right)

            if node.left is not None:
                node_lst.append(node.left)

        print(leaves)

        node_lst: list[TreeNode] = [root2]

        while node_lst:
            node = node_lst.pop()
            if node.left is None and node.right is None:
                try:
                    if leaves.pop(0) != node.val:
                        return False
                except Exception:
                    return False

            if node.right is not None:
                node_lst.append(node.right)

            if node.left is not None:
                node_lst.append(node.left)

        if len(leaves) > 0:
            return False

        return True
