#53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)
        local_max = 0
        global_max = 0
        for num in nums:
            local_max = max(0, num + local_max)
            global_max = max (global_max, local_max)
        return global_max

#88. Merge Sorted Array
