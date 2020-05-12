"""
[My Solution]
Runtime: 76 ms, faster than 46.02% of Python3 online submissions for Single Element in a Sorted Array.
Memory Usage: 16.2 MB, less than 7.69% of Python3 online submissions for Single Element in a Sorted Array.
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        a = []
        for i in range(len(nums)):
            if nums[i] not in a:
                a.append(nums[i])
            else:
                a.remove(nums[i])
        return a[0]


"""
Runtime: 56 ms, faster than 99.86% of Python3 online submissions for Single Element in a Sorted Array.
Memory Usage: 16.2 MB, less than 7.69% of Python3 online submissions for Single Element in a Sorted Array.
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        
        while(left < right):
            mid = ((left + right)//4) * 2
            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]
