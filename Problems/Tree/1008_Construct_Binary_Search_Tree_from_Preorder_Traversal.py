"""
Runtime: 36 ms, faster than 62.89% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
Memory Usage: 13.7 MB, less than 6.67% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while (i < len(preorder)):
            if preorder[i] > preorder[0]:
                break
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
