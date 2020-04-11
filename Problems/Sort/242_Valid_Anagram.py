"""
Runtime: 40 ms, faster than 83.89% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.4 MB, less than 6.25% of Python3 online submissions for Valid Anagram.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return "".join(sorted(s)) == "".join(sorted(t))
