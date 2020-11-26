"""
Runtime: 48 ms, faster than 97.33% of Python online submissions for Minimum Size Subarray Sum.
Memory Usage: 15.5 MB, less than 26.68% of Python online submissions for Minimum Size Subarray Sum.
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        res = len(nums)+1
        total = 0
        while right < len(nums):
            total += nums[right]
            while total >= s:
                res = min(res, right-left+1)
                total -= nums[left]
                left += 1
            right += 1
        return res if res <=len(nums) else 0
