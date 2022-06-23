import collections
from typing import Optional, List

from data_struct.tree import to_binary_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []

        stack = [(root, 0)]
        node_count_dict = collections.defaultdict(int)
        res_dict = collections.defaultdict(int)
        while stack:
            node, level = stack.pop(0)
            res_dict[level] += node.val
            node_count_dict[level] += 1
            if node.left is not None:
                stack.append((node.left, level + 1))
            if node.right is not None:
                stack.append((node.right, level + 1))
        return [res_dict[k] / node_count_dict[k] for k in res_dict]


if __name__ == '__main__':
    s = Solution()
    print(s.averageOfLevels(to_binary_tree([3, 9, 20, None, None, 15, 7])))
