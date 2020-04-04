"""
[My Solution]
Runtime: 228 ms, faster than 12.03% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.1 MB, less than 5.97% of Python3 online submissions for Move Zeroes.
"""

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


"""
Runtime: 36 ms, faster than 99.52% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.1 MB, less than 5.97% of Python3 online submissions for Move Zeroes.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0 
        for num in range(len(nums)):
            if nums[num] != 0:
                nums[num], nums[pos] = nums[pos], nums[num]
                pos = pos + 1
        return nums
