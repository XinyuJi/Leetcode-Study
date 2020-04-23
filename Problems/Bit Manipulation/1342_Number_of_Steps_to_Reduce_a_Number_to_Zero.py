"""
Runtime: 32 ms, faster than 66.67% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
"""

class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        if num == 0:
            return 0
        else:
            while(num>0):
                if (num % 2) == 0:
                    num = num/2
                    count +=1
                else:
                    num = num -1
                    count +=1
            return count