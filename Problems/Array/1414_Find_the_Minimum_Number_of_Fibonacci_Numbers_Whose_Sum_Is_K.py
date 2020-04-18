"""
Runtime: 40 ms, faster than 50.00% of Python3 online submissions for Find the Minimum Number of Fibonacci Numbers Whose Sum Is K.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Find the Minimum Number of Fibonacci Numbers Whose Sum Is K.
"""

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        find = [1,1]
        count = 0
        while(find[-1]<k):
            find.append(find[-1] + find[-2])
        while(find and k):
            x = find.pop()
            if k >= x:
                k = k - x
                count = count +1
                
        return count
