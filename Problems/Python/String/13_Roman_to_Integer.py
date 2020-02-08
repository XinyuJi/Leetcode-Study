"""
Runtime: 48 ms, faster than 53.85% of Python3 online submissions for Roman to Integer.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Roman to Integer.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        count = 0
        for i in range(len(s)-1):
            if Roman[s[i]] < Roman[s[i+1]]:
                count = count - Roman[s[i]]
            else:
                count = count + Roman[s[i]]
        count = count + Roman[s[-1]]
        return count
