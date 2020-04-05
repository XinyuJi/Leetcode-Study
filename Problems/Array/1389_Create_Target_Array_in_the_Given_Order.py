"""
Runtime: 36 ms, faster than 35.89% of Python3 online submissions for Create Target Array in the Given Order.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Create Target Array in the Given Order.
"""

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        new_list = []
        for i in range(len(nums)):
            new_list.insert(index[i], nums[i])
        return new_list
