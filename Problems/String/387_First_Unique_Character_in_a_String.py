"""
Runtime: 156 ms, faster than 31.36% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 13.9 MB, less than 6.52% of Python3 online submissions for First Unique Character in a String.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1

        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1
