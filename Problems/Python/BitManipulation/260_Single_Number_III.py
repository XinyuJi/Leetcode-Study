"""
Runtime: 56 ms, faster than 89.44% of Python3 online submissions for Single Number III.
Memory Usage: 15.5 MB, less than 50.00% of Python3 online submissions for Single Number III.
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dictionary = {}
        for num in nums:
            if num in dictionary.keys():
                del dictionary[num]
            else:
                dictionary[num] = 1
        return list(dictionary.keys())
