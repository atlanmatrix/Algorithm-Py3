import functools
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        return functools.reduce(lambda x, y: x + y, [self.postorder(child) for child in root.children or []], []) + [root.val]
