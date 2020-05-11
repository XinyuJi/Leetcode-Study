"""
Runtime: 32 ms, faster than 84.69% of Python3 online submissions for Largest Number At Least Twice of Others.
Memory Usage: 13.8 MB, less than 20.00% of Python3 online submissions for Largest Number At Least Twice of Others.
"""

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if max(nums) < 2 * nums[i] and max(nums) != nums[i]:
                return -1
        return nums.index(max(nums))
