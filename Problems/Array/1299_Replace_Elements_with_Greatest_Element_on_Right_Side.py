"""
Runtime: 128 ms, faster than 76.81% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-2, -1, -1):
            arr[i] = max(arr[i+1], arr[i])
        return arr[1:]+[-1]
