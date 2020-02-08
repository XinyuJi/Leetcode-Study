"""
Runtime: 64 ms, faster than 52.75% of Python3 online submissions for Palindrome Number.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Palindrome Number.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            if x == int(str(x)[::-1]):
                return True
            else:
                return False
        else:
            return False
