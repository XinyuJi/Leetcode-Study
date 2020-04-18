"""
[My Solution]
Runtime: 216 ms, faster than 74.27% of Python3 online submissions for Valid Mountain Array.
Memory Usage: 15 MB, less than 5.26% of Python3 online submissions for Valid Mountain Array.
"""

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False

        a = max(A)
        index = A.index(a)
        if index == 0 or index == len(A)-1:
            return False
        
        for i in range(0, index-1):
            if A[i] >= A[i+1]:
                return False

        for i in range(index, len(A)-1):
            if A[i] <= A[i+1]:
                return False
        
        return True
