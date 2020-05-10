"""
Runtime: 772 ms, faster than 88.55% of Python3 online submissions for Find the Town Judge.
Memory Usage: 18.4 MB, less than 10.00% of Python3 online submissions for Find the Town Judge.
"""

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        ct = [0] * (N+1)
        for x, y in trust:
            ct[x] -= 1
            ct[y] += 1
        for i in range(1, N+1):
            if ct[i] == N-1:
                return i
        return -1
