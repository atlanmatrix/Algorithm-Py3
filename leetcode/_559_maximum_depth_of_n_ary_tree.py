"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        stack = [(root, 1)]
        max_level = 0
        while stack:
            node, level = stack.pop(0)
            max_level = max(max_level, level)
            if node.children:
                for sub_node in node.children:
                    stack.append((sub_node, level + 1))

        return  max_level
