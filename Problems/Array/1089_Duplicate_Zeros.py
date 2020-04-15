"""
[My Solution]
Runtime: 68 ms, faster than 80.98% of Python3 online submissions for Duplicate Zeros.
Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Duplicate Zeros.
"""

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        a = len(arr)-1
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == 0:
                arr.insert(i, 0)
        for i in range(len(arr)-1, a, -1):
            del arr[i]


"""
Runtime: 72 ms, faster than 57.62% of Python3 online submissions for Duplicate Zeros.
Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Duplicate Zeros.
"""

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while (i < len(arr)):
            if arr[i] == 0:
                i+=1
                arr.pop()
                arr.insert(i,0)
            i += 1
