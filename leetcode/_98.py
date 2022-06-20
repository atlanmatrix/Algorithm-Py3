from typing import Optional

from data_struct.tree import TreeNode, to_binary_tree


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def inner(root, val):
            if root.left is not None and (root.left.val > root.val):
                return False

            if root.right is not None and root.right.val < root.val:
                return False

            return inner(root.left) and inner(root.right)


if __name__ == "__main__":
    s = Solution()
    print(s.isValidBST(to_binary_tree([5,4,6,None,None,3,7])))
