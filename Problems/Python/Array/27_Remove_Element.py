"""
Runtime: 32 ms, faster than 57.07% of Python3 online submissions for Remove Element.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Element.
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x=0
        length = len(nums)
        while x < length:
            if nums[x] == val:
                del nums[x]
                x = x -1
                length-=1
            x+=1
        return len(nums)


"""
Testing Code

nums = [3,2,2,3]
val = 3
nums2 = [0,1,2,2,3,0,4,2]
val2 = 2

length=len(nums2)
x = 0

while x < length:
    if nums2[x] == val2:
        del nums2[x]
        x = x -1
        length-=1
    x+=1
print (nums2)
"""
