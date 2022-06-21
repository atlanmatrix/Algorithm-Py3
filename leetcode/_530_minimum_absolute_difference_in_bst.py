from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder_visit(node):
            if node is None:
                return []

            return inorder_visit(node.left) + [node.val] + inorder_visit(node.right)

        sorted_lst = inorder_visit(root)
        min_diff = 10000
        for i in range(len(sorted_lst) - 1):
            new_diff = sorted_lst[i + 1] - sorted_lst[i]
            if new_diff < min_diff:
                min_diff = new_diff

        return min_diff


if __name__ == "__main__":
    s = Solution()
    # print(s.getMinimumDifference())
