"""
Runtime: 36 ms, faster than 94.71% of Python online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.4 MB, less than 17.22% of Python online submissions for Longest Substring Without Repeating Characters.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        count = 0
        slow = 0
        for i in range(len(s)):
            if s[i] in dic and slow <= dic[s[i]]:
                slow = dic[s[i]] + 1
            else:
                count = max(count, i-slow+1)
            dic[s[i]] = i
        return count
