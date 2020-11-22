"""
Runtime: 68 ms, faster than 58.67% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.6 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.
"""

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

#####2020.11.22#####
"""
Runtime: 40 ms, faster than 97.24% of Python online submissions for Maximum Subarray.
Memory Usage: 14.4 MB, less than 34.83% of Python online submissions for Maximum Subarray.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        current = nums[0]
        MaxSum = nums[0]
        
        for num in nums[1:]:
            if (num + current > current) and (num + current > num):
                current += num
            else:
                MaxSum = max(current, MaxSum)
                current = max(num, current+num)

        return max(MaxSum, current)
