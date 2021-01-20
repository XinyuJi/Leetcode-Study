"""
Runtime: 920 ms, faster than 69.35% of Python online submissions for Longest Palindromic Substring.
Memory Usage: 13.7 MB, less than 53.71% of Python online submissions for Longest Palindromic Substring.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            for k in range(2):
                tmp = self.search(s, i, i+k)
                if len(tmp) > len(res):
                    res = tmp
        return res
    
    def search(self, s, a, b):
        while a >=0 and b < len(s) and s[a] == s[b]:
            a -= 1
            b += 1
        return s[a+1:b]
