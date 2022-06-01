from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def to_binary_tree(items: list[int]) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def visit(node: TreeNode, direct: str='l2r') -> list:
            if node is None or (node is not None and node.val is None):
                return [None]

            if direct == 'l2r':
                return [node.val] + visit(node.left) + visit(node.right)
            else:
                return [node.val] + visit(node.right, 'r2l') + visit(node.left, 'r2l')

        return visit(root.left) == visit(root.right, 'r2l')


if __name__ == "__main__":
    root = to_binary_tree([2,3,3,4,5,5,4,None,None,8,9,9,8])
    s = Solution()
    print(s.isSymmetric(root))
