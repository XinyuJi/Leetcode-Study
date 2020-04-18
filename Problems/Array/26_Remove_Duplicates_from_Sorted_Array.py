"""
Runtime: 112 ms, faster than 15.87% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 14.5 MB, less than 97.54% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)


"""
[My Solution] After 3 months of 1st 
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

"""
[My Solution 2] After 13 days from 2nd Solution
Runtime: 100 ms, faster than 30.55% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.4 MB, less than 5.74% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        a = 1
        while(a < len(nums)):
            b = nums[a-1]
            if nums[a] != b: 
                a = a + 1
            else: 
                del nums[a]
        return len(nums)
