class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_count = collections.Counter(ransomNote)
        mag_count = collections.Counter(magazine)
        return ran_count & mag_count == ran_count
