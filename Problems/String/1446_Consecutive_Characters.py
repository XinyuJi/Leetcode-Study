"""
Runtime: 40 ms, faster than 92.93% of Python3 online submissions for Consecutive Characters.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Consecutive Characters.
"""

class Solution:
    def maxPower(self, s: str) -> int:
        i = 1
        count = 0
        max_count = 0
        while i < len(s):
            if s[i] == s[i-1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
            i += 1
        return max_count + 1
