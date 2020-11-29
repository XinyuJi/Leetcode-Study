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