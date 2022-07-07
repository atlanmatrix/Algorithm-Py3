import collections
from typing import Optional

from data_struct.tree import to_binary_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        my_queue = collections.deque([(root, 0, None)])
        known_level = -1
        known_parent = None
        while my_queue:
            node, level, p_val = my_queue.popleft()
            if node.val in (x, y):
                if known_level != -1 and level != known_level:
                    # Find second one does not match
                    return False
                elif known_level != -1:
                    # Find second one match
                    if known_parent == p_val:
                        # But they are brothers(not cousins)
                        return False
                    return True
                else:
                    # find first one
                    known_level = level
                    known_parent = p_val
            if node.left is not None:
                my_queue.append((node.left, level + 1, node.val))
            if node.right is not None:
                my_queue.append((node.right, level + 1, node.val))


if __name__ == '__main__':
    s = Solution()
    print(s.isCousins(to_binary_tree([1, 2, 3, 4]), 4, 3))
    print(s.isCousins(to_binary_tree([1, 2, 3, None, 4, None, 5]), 4, 5))
    print(s.isCousins(to_binary_tree([1, 2, 3, None, 4]), 2, 3))
