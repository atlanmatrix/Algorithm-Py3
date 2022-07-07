from typing import Optional

from data_struct.tree import to_binary_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST2(self, root: Optional[TreeNode]) -> int:
        self.min_val = float('inf')

        def dfs(node):
            if node is None:
                return None, None

            min_left_val, max_left_val = dfs(node.left)
            min_right_val, max_right_val = dfs(node.right)

            candi_lst = [self.min_val]
            if max_left_val:
                candi_lst.append(node.val - max_left_val)
            if min_right_val:
                candi_lst.append(min_right_val - node.val)
            self.min_val = min(candi_lst)
            return min_left_val or node.val, max_right_val or node.val

        dfs(root)
        return self.min_val

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def fn(node, lo, hi):
            if not node: return hi - lo
            left = fn(node.left, lo, node.val)
            right = fn(node.right, node.val, hi)
            print(node.val, left, right)
            return min(left, right)

        return fn(root, float('-inf'), float('inf'))



if __name__ == '__main__':
    s = Solution()
    print(s.minDiffInBST(to_binary_tree([90,69,None,49,89,None,52])))
