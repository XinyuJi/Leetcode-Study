class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        x = len(grid)
        y = len(grid[0])
        
        def dfs(grid, i, j):
            grid[i][j] = "0"
            directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
            for xi, yj in directions:
                    new_x = xi + i
                    new_y = yj + j
                    if new_x >= 0 and new_x < x and new_y >= 0 and new_y < y and grid[new_x][new_y] == "1":
                        dfs(grid, new_x, new_y)
            return
        
        count = 0
        for a in range(x):
            for b in range(y):
                if grid[a][b] == "1":
                    count += 1
                    dfs(grid, a, b)
        return count
