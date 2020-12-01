"""
Runtime: 16 ms, faster than 72.25% of Python online submissions for Spiral Matrix.
Memory Usage: 13.4 MB, less than 73.89% of Python online submissions for Spiral Matrix.
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])
