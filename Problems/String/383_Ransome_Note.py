"""
Runtime: 44 ms, faster than 76.79% of Python3 online submissions for Ransom Note.
Memory Usage: 13.9 MB, less than 25.00% of Python3 online submissions for Ransom Note.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_count = collections.Counter(ransomNote)
        mag_count = collections.Counter(magazine)
        return ran_count & mag_count == ran_count
