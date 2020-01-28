"""
Runtime: 48 ms, faster than 74.24% of Python3 online submissions for Search Insert Position.
Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Search Insert Position.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)


"""
Testing Code

list1 = [1,3,5,6]
val = 6
list1 = [1,3,5,6]
val = 2
list1 = [1,3,5,6]
val = 7
list1 = [1,3,5,6]
val = 0

if val in list1:
    print (list1.index(val))
else:
    list1.append(val)
    list1.sort()
    print(list1.index(val))
"""
