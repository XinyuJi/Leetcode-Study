"""
[Left and Right product lists] - 根据算法自己写
Runtime: 116 ms, faster than 94.32% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 20.4 MB, less than 84.00% of Python3 online submissions for Product of Array Except Self.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        output = [1]
        for i in range(1,len(nums)):
            left = output[i-1]*nums[i-1]
            output.append(left)

        right = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            output[i] = output[i] * right
            right = right * nums[i] 

        return output
        