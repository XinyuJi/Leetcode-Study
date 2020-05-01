"""
Runtime: 28 ms, faster than 68.37% of Python3 online submissions for First Bad Version.
Memory Usage: 13.8 MB, less than 6.90% of Python3 online submissions for First Bad Version.
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while(start<end):
            mid = (start+end)//2
            if isBadVersion(mid) is True:
                end = mid
            else:
                start = mid + 1
        return start
