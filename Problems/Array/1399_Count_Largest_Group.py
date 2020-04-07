"""
Runtime: 132 ms, faster than 41.37% of Python3 online submissions for Count Largest Group.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Count Largest Group.
"""

class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = {}
        count = 0
        for a in range(1,n+1):
            key = sum([int(i) for i in str(a)])
            if key not in dic:
                dic[key] = 1
            else:
                dic[key] = dic[key] + 1
        for i in dic.values():
            if i == max(dic.values()):
                count =count + 1
        return count
