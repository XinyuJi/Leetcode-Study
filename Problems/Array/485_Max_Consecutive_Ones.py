"""
Runtime: 388 ms, faster than 47.53% of Python3 online submissions for Max Consecutive Ones.
Memory Usage: 13.9 MB, less than 7.69% of Python3 online submissions for Max Consecutive Ones.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count
