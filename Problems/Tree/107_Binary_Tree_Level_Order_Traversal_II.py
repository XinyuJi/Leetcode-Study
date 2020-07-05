"""
Runtime: 28 ms, faster than 33.09% of Python online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 13.1 MB, less than 88.50% of Python online submissions for Binary Tree Level Order Traversal II.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, q = [], [root]
        while q:
            val, temp = [], []
            for node in q:
                val.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(val)
            q = temp
        return res[::-1]
