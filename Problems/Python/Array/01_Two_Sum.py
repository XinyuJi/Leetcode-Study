"""
Runtime: 1408 ms, faster than 22.67% of Python3 online submissions for Two Sum.
Memory Usage: 13.5 MB, less than 99.07% of Python3 online submissions for Two Sum.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target - nums[i]) in nums and nums.index(target - nums[i])!=i:
                return i, nums.index(target - nums[i])


#Dictionary
"""
Runtime: 48 ms, faster than 79.50% of Python3 online submissions for Two Sum.
Memory Usage: 14.2 MB, less than 54.88% of Python3 online submissions for Two Sum.
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary={}
        for i in range(len(nums)):
            if target - nums[i] not in dictionary:
                dictionary[nums[i]]=i
            else:
                return [dictionary[target - nums[i]], i]
