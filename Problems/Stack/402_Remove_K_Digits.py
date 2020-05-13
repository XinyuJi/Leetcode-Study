"""
Runtime: 32 ms, faster than 90.71% of Python3 online submissions for Remove K Digits.
Memory Usage: 14 MB, less than 11.11% of Python3 online submissions for Remove K Digits.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        if len(num) == k:
            return '0'
        
        for n in num:
            while k > 0 and stack and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)
        
        for i in range(k):
            stack.pop()

        return ''.join(stack).lstrip('0') or '0'
