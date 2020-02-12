"""
Runtime: 28 ms, faster than 70.17% of Python online submissions for Search in Rotated Sorted Array.
Memory Usage: 12 MB, less than 48.98% of Python online submissions for Search in Rotated Sorted Array.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


"""
Runtime: 28 ms, faster than 70.17% of Python online submissions for Search in Rotated Sorted Array.
Memory Usage: 12.2 MB, less than 6.12% of Python online submissions for Search in Rotated Sorted Array.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            return -1
