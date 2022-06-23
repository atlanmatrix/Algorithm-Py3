from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


    def mergeTrees2(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2

        if root2 is None:
            return root1

        def dfs(node1, node2):
            if node2 is None:
                return
            node1.val += node2.val
            if node1.left is None:
                node1.left = node2.left
                if node1.right is not None:
                    dfs(node1.right, node2.right)
                else:
                    node1.right = node2.right
            else:
                dfs(node1.left, node2.left)
                if node1.right is not None:
                    dfs(node1.right, node2.right)
                else:
                    node1.right = node2.right
        dfs(root1, root2)
        return root1


if __name__ == '__main__':
    pass
