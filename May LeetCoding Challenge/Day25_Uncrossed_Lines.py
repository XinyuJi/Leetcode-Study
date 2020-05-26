class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        DP = [[0 for j in range(len(B))] for i in range(len(A))]
        for i, a in enumerate(A):
            for j, b in enumerate(B):
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])
                if a == b:
                    if i >= 1 and j >= 1:
                        DP[i][j] = max(DP[i-1][j-1]+1, DP[i][j])
                    else:
                        DP[i][j] = 1
        return DP[-1][-1]
