"""
Runtime: 56 ms, faster than 97.35% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Two Sum II - Input array is sorted.
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicts={}
        for i in range(len(numbers)):
            if target - numbers[i] not in dicts:
                dicts[numbers[i]] = i + 1
            else:
                return [dicts[target-numbers[i]], i+1]
