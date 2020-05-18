"""
Runtime: 36 ms, faster than 94.85% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
"""

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
        return count
