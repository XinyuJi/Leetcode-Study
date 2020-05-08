class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        
        if coordinates[0][0] == coordinates[1][0]:
            m = 0
        else:
            m = (coordinates[1][1]-coordinates[0][1]) / (coordinates[1][0]-coordinates[0][0])
        k = coordinates[0][1] - ( m * coordinates[0][0])

        for i in range(2, len(coordinates)):
            if (coordinates[i][0] - coordinates[0][0]) == 0:
                m2 = 0
            else:
                m2 = (coordinates[i][1] - coordinates[0][1]) / (coordinates[i][0] - coordinates[0][0])
            k2 = coordinates[0][1] - ( coordinates[0][0] * m2)
            if m2 != m or k2 != k:
                return False
        return True
