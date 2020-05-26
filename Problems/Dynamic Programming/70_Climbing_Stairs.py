"""
Runtime: 32 ms, faster than 45.65% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.9 MB, less than 5.97% of Python3 online submissions for Climbing Stairs.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a+b
        return a