class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for num in range(0, len(nums)):
            if nums[num] == 0:
                nums.remove(0)
                nums.append(0)
        return nums
