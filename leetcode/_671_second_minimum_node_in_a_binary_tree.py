from typing import Optional

from data_struct.tree import to_binary_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        """
        Return -1 if children are the same
        """
        if root is None:
            return -1
        elif root.left is None:
            return -1
        elif root.left.val != root.right.val:
            if root.left.val < root.right.val:
                l_val = self.findSecondMinimumValue(root.left)
                return root.right.val if l_val == -1 else min(root.right.val, l_val)
            else:
                r_val = self.findSecondMinimumValue(root.right)
                return root.left.val if r_val == -1 else min(root.left.val, r_val)
        else:
            l_val = self.findSecondMinimumValue(root.left)
            r_val = self.findSecondMinimumValue(root.right)

            if l_val == -1 and r_val == -1:
                return -1
            elif l_val == -1:
                return r_val
            elif r_val == -1:
                return l_val
            else:
                return min([l_val, r_val])

    def findSecondMinimumValue2(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return

            if node.val != self.min_val and node.val < self.s_min_val:
                self.s_min_val = node.val
            dfs(node.left)
            dfs(node.right)

        self.min_val = root.val
        self.s_min_val = float('inf')
        dfs(root)
        return -1 if self.s_min_val == float('inf') else self.s_min_val

    def findSecondMinimumValue3(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1

        node_lst = []

        def dfs(node):
            if node is None:
                return

            node_lst.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        node_lst = sorted(list(set(node_lst)))
        return -1 if len(node_lst) < 2 else node_lst[1]


if __name__ == "__main__":
    s = Solution()
    print(s.findSecondMinimumValue(to_binary_tree(
[1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1])))
