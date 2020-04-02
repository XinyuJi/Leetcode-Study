"""
Runtime: 120 ms, faster than 93.83% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for lists in grid:
            for item in lists:
                if item<0:
                    count = count +1
        return count
