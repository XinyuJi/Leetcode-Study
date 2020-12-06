"""
Runtime: 144 ms, faster than 26.04% of Python online submissions for Search a 2D Matrix II.
Memory Usage: 19.5 MB, less than 11.70% of Python online submissions for Search a 2D Matrix II.
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        j = -1
        for row in matrix:
            while j + len(row) >= 0 and row[j] > target:
                j -= 1
            if j + len(row) >= 0 and row[j] == target:
                return True
        return False
