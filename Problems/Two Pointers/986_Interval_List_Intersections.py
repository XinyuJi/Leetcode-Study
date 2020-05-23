"""
Runtime: 152 ms, faster than 89.05% of Python3 online submissions for Interval List Intersections.
Memory Usage: 14.4 MB, less than 6.06% of Python3 online submissions for Interval List Intersections.
"""

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        res = []
        while i < len(A) and j < len(B):
            if A[i][1] < B[j][0]:
                i += 1
            elif A[i][0] > B[j][1]:
                j += 1
            else:
                res.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
                if A[i][1] > B[j][1]:
                    j += 1
                else:
                    i += 1
        return res
