"""
Runtime: 24 ms, faster than 43.85% of Python online submissions for Subsets.
Memory Usage: 13.5 MB, less than 94.15% of Python online submissions for Subsets.
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result
