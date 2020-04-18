class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        x = len(grid)
        y = len(grid[0])
        
        for i in range(x):
            for j in range(y):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif j == 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i][j-1], grid[i-1][j])

        return grid[x-1][y-1]
