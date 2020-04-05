"""
Runtime: 112 ms, faster than 15.87% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 14.5 MB, less than 97.54% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)


"""
[My Solution]
Runtime: 788 ms, faster than 7.06% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.6 MB, less than 5.74% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        pos = 1
        container = nums[0]
        while(pos < len(nums)):
            if nums[pos] == container:
                nums.remove(nums[pos])
                if pos > 0:
                    pos = pos -1
            else:
                container = nums[pos]
            pos = pos +1 
        return len(nums)
