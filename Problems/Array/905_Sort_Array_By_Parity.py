"""
Runtime: 80 ms, faster than 77.54% of Python3 online submissions for Sort Array By Parity.
Memory Usage: 14.4 MB, less than 5.19% of Python3 online submissions for Sort Array By Parity.
"""

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        pos = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[i], A[pos] = A[pos], A[i]
                pos += 1
        return A
