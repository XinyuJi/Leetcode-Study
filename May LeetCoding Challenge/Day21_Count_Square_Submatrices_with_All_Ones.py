class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        new_m = [[0]*(n+1) for _ in range(m+1)]
        
        for row in range(1, m+1):
            for col in range(1, n+1):
                if matrix[row-1][col-1] == 1:
                    new_m[row][col] = min(new_m[row-1][col-1], new_m[row-1][col], new_m[row][col-1])+1
                    count += new_m[row][col]
        return count
