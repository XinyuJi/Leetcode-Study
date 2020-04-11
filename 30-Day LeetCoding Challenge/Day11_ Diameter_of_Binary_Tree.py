# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_path = 0
        def tree_depth(root):
            if not root:
                return 0
            left = tree_depth(root.left)
            right = tree_depth(root.right)
            self.max_path = max(self.max_path, left+right)
            return 1+max(left, right)
        tree_depth(root)
        return self.max_path
