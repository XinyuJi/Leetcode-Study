"""
Runtime: 552 ms, faster than 7.51% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[i]>nums[j]:
                    count = count +1
            result.append(count)
        return result
