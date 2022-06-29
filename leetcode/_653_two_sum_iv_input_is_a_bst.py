from typing import Optional

from data_struct.tree import to_binary_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(node):
            if node is None:
                return []

            return dfs(node.left) + [node.val] + dfs(node.right)

        lst = dfs(root)
        s = 0
        e = len(lst) - 1
        while s < e:
            sum = lst[s] + lst[e]
            if sum == k:
                return True
            elif sum > k:
                e -= 1
            else:
                s += 1
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.findTarget(to_binary_tree([5, 3, 6, 2, 4, None, 7]), 12))
