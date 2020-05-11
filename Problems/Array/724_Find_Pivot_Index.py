"""
Runtime: 4636 ms, faster than 14.26% of Python3 online submissions for Find Pivot Index.
Memory Usage: 14.9 MB, less than 8.33% of Python3 online submissions for Find Pivot Index.
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = [0, ]
        a = 0
        for i in range(1, len(nums)):
            a = a + nums[i-1]
            left.append(a)


        right = [0,]
        a = 0
        for i in range(len(nums)-1, -1, -1):
            a = a + nums[i]
            right.append(a)
        del right[-1]

        for i in range(len(nums)):
            if left[i] == right[::-1][i]:
                return i
        return -1
