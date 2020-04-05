"""
Runtime: 252 ms, faster than 5.77% of Python3 online submissions for Find Lucky Integer in an Array.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Find Lucky Integer in an Array.
"""

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        num = 0
        for i in arr:
            if arr.count(i) == i:
                num = max(num, i)
        if num == 0:
            return -1
        else:
            return num
