from typing import Optional

from data_struct.tree import TreeNode, to_binary_tree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val == root.val:
            return p

        if q.val == root.val:
            return q

        if (p.val - root.val) * (q.val - root.val) < 0:
            return root
        elif p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)


if __name__ == "__main__":
    s = Solution()
    print(s.lowestCommonAncestor(
        to_binary_tree([6,2,8,0,4,7,9,None,None,3,5]),
        TreeNode(2),
        TreeNode(8)
    ).val)
    print(s.lowestCommonAncestor(
        to_binary_tree([6,2,8,0,4,7,9,None,None,3,5]),
        TreeNode(2),
        TreeNode(4)
    ).val)
    print(s.lowestCommonAncestor(
        to_binary_tree([2,1]),
        TreeNode(2),
        TreeNode(1)
    ).val)
