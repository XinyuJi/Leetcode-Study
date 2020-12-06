"""
Runtime: 24 ms, faster than 44.86% of Python online submissions for Number of Good Pairs.
Memory Usage: 13.4 MB, less than 71.37% of Python online submissions for Number of Good Pairs.
"""

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        count = 0
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        for num in dic:
            val = dic[num]
            for i in range(val):
                count += i
        return count
