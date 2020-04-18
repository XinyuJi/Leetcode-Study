"""
Runtime: 60 ms, faster than 50.00% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
"""

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start_number = 1
        count = start_number
        i = 0
        while(i <= len(nums)-1):
            count = count  + nums[i]
            if count  < 1:
                start_number = start_number + 1
                count = start_number
                i = 0
            else:
                i += 1

        return start_number
