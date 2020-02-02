"""
Runtime: 28 ms, faster than 78.42% of Python3 online submissions for Reverse Integer.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Reverse Integer.
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            result = int(str(x)[::-1])
        else:
            result = -int(str(x)[1:][::-1])
        
        if -2**31 <= result <= (2**31)-1:
            return result
        else:
            return 0