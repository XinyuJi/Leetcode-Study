"""
Runtime: 76 ms, faster than 53.85% of Python3 online submissions for Check If N and Its Double Exist.
Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Check If N and Its Double Exist.
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        a = []
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i!= j and arr[i] == 2* arr[j]:
                    return True
