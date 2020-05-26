"""
Runtime: 32 ms, faster than 59.66% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.7 MB, less than 5.80% of Python3 online submissions for Fibonacci Number.
"""

class Solution:
    def fib(self, N: int) -> int:
        a = 1
        b = 1
        if N == 0:
            return 0
        
        elif 0 < N <= 2:
            return 1
        
        for i in range(2, N):
            a, b = b, a + b
        return b
