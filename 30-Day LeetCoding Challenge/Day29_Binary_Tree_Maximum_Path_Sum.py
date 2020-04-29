# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def traversal(root):
            if not root:
                return 0
            left = max(0, traversal(root.left))
            right = max(0, traversal(root.right))
            self.res = max(self.res, left+right+root.val)
            return max(left, right, 0) + root.val
        self.res = float('-inf')
        traversal(root)
        return self.res
