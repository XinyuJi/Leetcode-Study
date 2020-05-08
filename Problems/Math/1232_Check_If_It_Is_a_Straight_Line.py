"""
Runtime: 64 ms, faster than 52.57% of Python3 online submissions for Check If It Is a Straight Line.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Check If It Is a Straight Line.
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        a, b = coordinates[0][0], coordinates[0][1]
        c, d = coordinates[1][0], coordinates[1][1]
        
        if a == c:
            m = 0
        else:
            m = (d-b) / (c-a)
        k = b - ( m * a)

        for i in range(2, len(coordinates)):
            if (coordinates[i][0] - a) == 0:
                m2 = 0
            else:
                m2 = (coordinates[i][1] - b) / (coordinates[i][0] - a)
            k2 = b - ( a * m2)
            if m2 != m or k2 != k:
                return False
        return True
