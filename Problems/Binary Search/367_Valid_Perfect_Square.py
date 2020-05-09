"""
Runtime: 32 ms, faster than 46.70% of Python3 online submissions for Valid Perfect Square.
Memory Usage: 13.6 MB, less than 10.00% of Python3 online submissions for Valid Perfect Square.
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num

        while left <= right:
            mid = (left+right)//2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                right = mid-1
            else:
                left = mid+1
        return False
