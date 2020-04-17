"""
Runtime: 140 ms, faster than 81.77% of Python3 online submissions for Number of Islands.
Memory Usage: 14.8 MB, less than 9.40% of Python3 online submissions for Number of Islands.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        x = len(grid)
        y = len(grid[0])
        
        def dfs(grid: List[List[str]], i:int, j:int) -> None:
            grid[i][j] = '0'
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for d_i, d_j in directions:
                new_i = i + d_i
                new_j = j + d_j
                if new_i >= 0 and new_i < x and new_j >= 0 and new_j < y and grid[new_i][new_j] == '1':
                    dfs(grid, new_i, new_j)
            return
        
        count = 0
        for i in range(x):
            for j in range(y):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid, i, j)
        return count
