from typing import Optional

from data_struct.tree import to_binary_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''
        t_s = ''

        if root.right is not None:
            t_s += f'({self.tree2str(root.left)})'
            t_s += f'({self.tree2str(root.right)})'
        elif root.left is not None:
            t_s += f'({self.tree2str(root.left)})'
        return f'{root.val}{t_s}'

        return self.tree2str(root)


if __name__ == '__main__':
    s = Solution()
    print(s.tree2str(to_binary_tree([1,2,3,4])))
    print(s.tree2str(to_binary_tree([1, 2, 3, None, 4])))
