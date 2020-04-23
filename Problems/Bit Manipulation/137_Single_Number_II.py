"""
[Dictionary]

Runtime: 60 ms, faster than 54.14% of Python3 online submissions for Single Number II.
Memory Usage: 15.4 MB, less than 6.67% of Python3 online submissions for Single Number II.
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary ={}
        for i in nums:
            if i in dictionary.keys():
                if dictionary[i] == 2:
                    del dictionary[i]
                else:
                    dictionary[i] = dictionary[i] +1  
            else:
                dictionary[i]=1
        return list(dictionary.keys())[0]


"""
[bitwise operation method for single numbers]

Runtime: 60 ms, faster than 54.14% of Python3 online submissions for Single Number II.
Memory Usage: 15.4 MB, less than 6.67% of Python3 online submissions for Single Number II.

https://blog.csdn.net/wlwh90/article/details/89712795
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x1 = 0
        x2 = 0
        for num in nums:
            x2 = x2 ^ (x1 & num)
            x1 = x1 ^ num
            mask = ~ (x1 & x2)
            x2 = x2 & mask
            x1 = x1 & mask
        return x1
