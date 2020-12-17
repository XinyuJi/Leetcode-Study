"""
Runtime: 20 ms, faster than 79.01% of Python online submissions for Sqrt(x).
Memory Usage: 13.4 MB, less than 66.34% of Python online submissions for Sqrt(x).
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l <= r:
            mid = (l+r)//2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            elif mid * mid < x:
                l = mid + 1
        return r
