from typing import Optional

from data_struct.tree import TreeNode, to_binary_tree


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root is None:
            return depth

        m: list[tuple[int, TreeNode]] = [(1, root)]
        while m:
            depth, node = m.pop(0)
            if node.left is None and node.right is None:
                return depth

            if node.left is not None:
                m.append((depth + 1, node.left))

            if node.right is not None:
                m.append((depth + 1, node.right))
        return depth


    def minDepth2(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        print(root.val, root.left, root.right)
        if root.left is None:
            if root.right is None:
                return 1
            else:
                return 1 + self.minDepth(root.right)
        if root.right is None:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


if __name__ == "__main__":
    s = Solution()
    print(s.minDepth(to_binary_tree([3,9,20,None,None,15,7])))
    print(s.minDepth(to_binary_tree([2,None,3,None,4,None,5,None,6])))
