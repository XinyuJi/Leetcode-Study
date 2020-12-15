"""
Runtime: 16 ms, faster than 94.69% of Python online submissions for Longest Common Prefix.
Memory Usage: 13.7 MB, less than 38.46% of Python online submissions for Longest Common Prefix.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        m, M = min(strs), max(strs)
        count = 0
        for i in range(min(len(m), len(M))):
            if m[i] != M[i]:
                break
            else:
                count += 1
        return m[:count]
