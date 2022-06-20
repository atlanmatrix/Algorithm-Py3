from logging import root
import functools
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        return (root and [root.val] + functools.reduce(lambda res, node: res + self.preorder(node), root and root.children or [], [])) or []
