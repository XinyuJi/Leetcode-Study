"""
Runtime: 20 ms, faster than 96.61% of Python3 online submissions for Length of Last Word.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Length of Last Word.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
