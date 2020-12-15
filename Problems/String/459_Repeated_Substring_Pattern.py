"""
Runtime: 480 ms, faster than 30.21% of Python online submissions for Repeated Substring Pattern.
Memory Usage: 13.9 MB, less than 49.55% of Python online submissions for Repeated Substring Pattern.
"""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s)//2+1):
            if s == s[i:] + s[:i]:
                return True
        return False

"""
Runtime: 20 ms, faster than 91.24% of Python online submissions for Repeated Substring Pattern.
Memory Usage: 13.9 MB, less than 49.55% of Python online submissions for Repeated Substring Pattern.
"""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in s[1:] + s[:-1]
