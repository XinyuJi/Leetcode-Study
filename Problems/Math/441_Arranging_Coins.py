"""
Runtime: 16 ms, faster than 97.70% of Python online submissions for Arranging Coins.
Memory Usage: 12.7 MB, less than 76.53% of Python online submissions for Arranging Coins.
"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((-1+(math.sqrt(1+8*n)))/2)
