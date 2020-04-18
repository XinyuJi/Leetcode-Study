"""
[My Soultion 1]
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

"""
[My Soultion 2] After 2 months, 1 week from 1st Solution
Runtime: 60 ms, faster than 21.77% of Python3 online submissions for Check If N and Its Double Exist.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Check If N and Its Double Exist.
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j] * 2 or arr[j] == arr[i] * 2 and i != j:
                    return True