from typing import Optional, List

from data_struct.tree import to_binary_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        res_lst = []

        def dfs(node, sum=0, s=''):
            sum += node.val
            s += ' ' + str(node.val)
            print(sum, s)
            if node.left is None and node.right is None:
                if sum == targetSum:
                    res_lst.append(s.strip().split(' '))
                return
            if node.left is not None:
                dfs(node.left, sum, s)
            if node.right is not None:
                dfs(node.right, sum, s)


        dfs(root)

        return res_lst


if __name__ == '__main__':
    s = Solution()
    print(s.pathSum(to_binary_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22))
