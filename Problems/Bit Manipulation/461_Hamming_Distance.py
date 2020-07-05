"""
Runtime: 20 ms, faster than 58.04% of Python online submissions for Hamming Distance.
Memory Usage: 12.8 MB, less than 20.15% of Python online submissions for Hamming Distance.
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
