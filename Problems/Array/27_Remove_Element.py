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
[My Solution]
Runtime: 28 ms, faster than 85.31% of Python3 online submissions for Remove Element.
Memory Usage: 14 MB, less than 6.06% of Python3 online submissions for Remove Element.
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num = 0
        while(num<len(nums)):
            if nums[num] == val:
                nums.remove(nums[num])
                if num > 0:
                    num = num - 1
                else:
                    num = num
            else:
                num = num + 1
        return len(nums)
