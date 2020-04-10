"""
Runtime: 20 ms, faster than 98.37% of Python3 online submissions for Backspace String Compare.
Memory Usage: 13.8 MB, less than 8.00% of Python3 online submissions for Backspace String Compare.
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = ''
        t = ''

        for i in S:
            if i == "#":
                s = s[:-1]
            else:
                s = s + i

        for j in T:
            if j == "#":
                t = t[:-1]
            else:
                t = t + j

        return s == t
