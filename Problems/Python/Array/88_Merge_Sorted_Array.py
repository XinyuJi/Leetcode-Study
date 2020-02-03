"""
Runtime: 36 ms, faster than 58.39% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.
"""

"""
    Do not return anything, modify nums1 in-place instead.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while len(nums1) > m:
            nums1.remove(nums1[len(nums1)-1])
        while len(nums2) > n:
            nums2.remove(nums2[len(nums2)-1])
        nums1.extend(nums2)
        nums1.sort()
