"""
Runtime: 48 ms, faster than 88.04% of Python3 online submissions for Third Maximum Number.
Memory Usage: 14.4 MB, less than 7.69% of Python3 online submissions for Third Maximum Number.
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        i = 0
        count = 1
        while( i <= len(nums)-2  and count<3):
            if nums[i] != nums[i+1]:
                count += 1
                i += 1
            else:
                del nums[i+1]

        if len(nums) < 3:
            return max(nums)
        else:
            return nums[i]
