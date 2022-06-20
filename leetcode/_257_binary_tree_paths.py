from typing import Optional, List

from data_struct.tree import TreeNode, to_binary_tree


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []

        root.val = str(root.val)
        if root.left is None and root.right is None:
            return [root.val]

        return [
            '->'.join([root.val] + [c])
            for c in self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        ]


if __name__ == "__main__":
    s = Solution()
    print(s.binaryTreePaths(to_binary_tree([1,2,3,None,5])))
    print(s.binaryTreePaths(to_binary_tree([1])))
