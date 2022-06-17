from typing import Optional

from data_struct.tree import TreeNode, to_binary_tree


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return root

        def inner(node):
            node.left, node.right = node.right, node.left
            if node.left is not None:
                inner(node.left)
            if node.right is not None:
                inner(node.right)

        inner(root)
        return root


if __name__ == "__main__":
    s = Solution()
    print(s.isValidBST(to_binary_tree(
        [4,2,7,1,3,6,9]
    )))
