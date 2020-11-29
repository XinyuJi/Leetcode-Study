######################################################################
#53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)
        local_max = 0
        global_max = 0
        for num in nums:
            local_max = max(0, num + local_max)
            global_max = max (global_max, local_max)
        return global_max

######################################################################
#88. Merge Sorted Array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m>0 and n>0:
            if nums2[n-1] > nums1[m-1]:
                nums1[m-1+n] = nums2[n-1]
                n -= 1
            else:
                nums1[m-1], nums1[m-1+n] = nums1[m-1+n], nums1[m-1]
                m -= 1
        
        if m == 0 and n > 0:
            nums1[:n] = nums2[:n]

