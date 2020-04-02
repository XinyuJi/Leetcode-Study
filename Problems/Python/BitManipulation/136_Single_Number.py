"""
[Bit Manipulation]
Runtime: 88 ms, faster than 65.22% of Python3 online submissions for Single Number.
Memory Usage: 16.3 MB, less than 6.56% of Python3 online submissions for Single Number.
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0
        for num in nums:
            output ^= num
        return output


"""
[Hash Table]
Runtime: 92 ms, faster than 39.83% of Python3 online submissions for Single Number.
Memory Usage: 16.4 MB, less than 6.56% of Python3 online submissions for Single Number.
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {}
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                del dictionary[num]
        return list(dictionary.keys())[0]
