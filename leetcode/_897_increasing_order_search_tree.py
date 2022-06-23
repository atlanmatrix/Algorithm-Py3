from data_struct.tree import to_binary_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node is None:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)

        res = dfs(root)
        curr = new_root = TreeNode()
        while res:
            curr.right = TreeNode(res.pop(0))
            curr = curr.right
        return new_root.right


if __name__ == '__main__':
    s = Solution()
    print(s.increasingBST(to_binary_tree([5,3,6,2,4,None,8,1,None,None,None,7,9])))
