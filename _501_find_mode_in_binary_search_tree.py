from typing import Optional, List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mode_dict: dict[int, int] = collections.defaultdict(int)
        def same_as_parent(node):
            if node is not None:
                mode_dict[node.val] += 1
                same_as_parent(node.left)
                same_as_parent(node.right)

        same_as_parent(root)

        max_mode = -1
        res_lst = []
        for k in mode_dict:
            if mode_dict[k] == max_mode:
                res_lst.append(k)
            elif mode_dict[k] > max_mode:
                res_lst = [k]
                max_mode = mode_dict[k]

        return res_lst


    def findMode2(self, root: Optional[TreeNode]) -> List[int]:
        def recursion(node):
            if node is None:
                return []

            return [node.val] + recursion(node.left) + recursion(node.right)

        l = recursion(root)
        res = collections.Counter(l).most_common()
        max_count = res[0][1]
        return [x for x, c in res if c == max_count]
