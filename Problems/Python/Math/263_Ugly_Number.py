"""
Runtime: 28 ms, faster than 76.20% of Python3 online submissions for Ugly Number.
Memory Usage: 13.8 MB, less than 6.67% of Python3 online submissions for Ugly Number.
"""

class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        elif num == 1:
            return True
        while (num % 2 == 0):
            num = num / 2
        while (num % 3 == 0):
            num = num / 3
        while (num % 5 == 0):
            num = num / 5
        if num == 1:
            return True
        else:
            return False
