"""
Runtime: 28 ms, faster than 75.61% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 13.8 MB, less than 5.41% of Python3 online submissions for Invert Binary Tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
