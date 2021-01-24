"""
Runtime: 100 ms, faster than 60.59% of Python online submissions for 3Sum Closest.
Memory Usage: 13.3 MB, less than 77.80% of Python online submissions for 3Sum Closest.
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if temp == target:
                    return temp
                if abs(temp-target) < abs(res-target):
                    res = temp
                if temp < target:
                    l += 1
                if temp > target:
                    r -= 1
        return res
