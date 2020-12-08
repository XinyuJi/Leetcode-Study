"""
Runtime: 32 ms, faster than 98.08% of Python online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13.6 MB, less than 86.17% of Python online submissions for Longest Substring Without Repeating Characters.
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
        for i, letter in enumerate(s):
            if letter in dic and slow <= dic[letter]:
                slow = dic[letter] + 1
            else:
                count = max(count, i-slow+1)
            dic[letter] = i
        return count
