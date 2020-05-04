"""
Runtime: 24 ms, faster than 89.09% of Python3 online submissions for Number Complement.
Memory Usage: 13.8 MB, less than 10.00% of Python3 online submissions for Number Complement.
"""

class Solution:
    def findComplement(self, num: int) -> int:
        x = 1
        while x <= num:
            x <<= 1
        return (x-1) ^ num
