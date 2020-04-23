"""
Runtime: 52 ms, faster than 82.23% of Python3 online submissions for Bitwise AND of Numbers Range.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Bitwise AND of Numbers Range.
"""

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        a = m
        i = 1

        while a+i < n+1:
            a &= a+i
            i *= 2
        return a
