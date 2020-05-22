"""
Runtime: 40 ms, faster than 75.14% of Python3 online submissions for Sort Characters By Frequency.
Memory Usage: 15 MB, less than 7.14% of Python3 online submissions for Sort Characters By Frequency.
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(k * v for k, v in sorted(Counter(s).items(), key=lambda x:x[1], reverse=True))
