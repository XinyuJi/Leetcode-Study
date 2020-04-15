"""
Runtime: 212 ms, faster than 98.79% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 15.3 MB, less than 5.95% of Python3 online submissions for Squares of a Sorted Array.
"""

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            A[i] = A[i] * A[i]
        return sorted(A)
