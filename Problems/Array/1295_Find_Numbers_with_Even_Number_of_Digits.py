"""
Runtime: 48 ms, faster than 90.95% of Python3 online submissions for Find Numbers with Even Number of Digits.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Find Numbers with Even Number of Digits.
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if len(list(str(nums[i]))) % 2 == 0:
                count += 1
        return count
