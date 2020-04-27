class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        DP = [[0]*(m+1) for k in range(n+1)]
        
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    DP[i+1][j+1] = DP[i][j] + 1
                else:
                    DP[i+1][j+1] = max(DP[i+1][j], DP[i][j+1])
        return DP[-1][-1]
