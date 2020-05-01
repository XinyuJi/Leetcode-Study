class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if reach < i:
                return False
            if reach >= len(nums)-1:
                return True
            reach = max(reach, i+nums[i])
