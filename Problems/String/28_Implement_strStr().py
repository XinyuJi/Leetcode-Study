"""
Runtime: 16 ms, faster than 83.17% of Python online submissions for Implement strStr().
Memory Usage: 13.7 MB, less than 63.37% of Python online submissions for Implement strStr().
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
