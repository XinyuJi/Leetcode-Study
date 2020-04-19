"""
Runtime: 344 ms, faster than 98.74% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 24.6 MB, less than 7.14% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1,len(nums)+1)) - set(nums))
