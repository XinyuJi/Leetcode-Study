"""
Runtime: 20 ms, faster than 96.30% of Python online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 13.5 MB, less than 85.55% of Python online submissions for Find Minimum in Rotated Sorted Array.
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
