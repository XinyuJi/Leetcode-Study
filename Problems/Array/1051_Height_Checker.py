"""
Runtime: 32 ms, faster than 78.29% of Python3 online submissions for Height Checker.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Height Checker.
"""

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        old = sorted(heights)
        count = 0

        for i in range(len(heights)):
            if old[i] != heights[i]:
                count += 1
        return count
