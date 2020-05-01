class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        if n == 0 or m == 0:
            return 0
        DP = [[0]*(m+1) for k in range(n+1)]
        res = 0


        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    DP[i+1][j+1] = min(DP[i][j], DP[i+1][j], DP[i][j+1]) + 1
                    res = max(res, DP[i+1][j+1])

        return res*res
