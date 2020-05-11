"""
Runtime: 24 ms, faster than 89.19% of Python3 online submissions for Number of Segments in a String.
Memory Usage: 13.9 MB, less than 6.67% of Python3 online submissions for Number of Segments in a String.
"""

class Solution:
    def countSegments(self, s: str) -> int:
        count = 0 
        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                count += 1
        return count


"""
Runtime: 28 ms, faster than 68.75% of Python3 online submissions for Number of Segments in a String.
Memory Usage: 13.8 MB, less than 6.67% of Python3 online submissions for Number of Segments in a String.
"""

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
