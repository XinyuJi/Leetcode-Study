"""
Runtime: 96 ms, faster than 39.52% of Python3 online submissions for Jump Game.
Memory Usage: 15.9 MB, less than 7.14% of Python3 online submissions for Jump Game.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if reach < i:
                return False
            if reach >= len(nums)-1:
                return True
            reach = max(reach, i+nums[i])
