"""
Return the number of islands which are connected vertically or horizotnally.
1. Need to find all independend islands.
2. Instead of coutnign number of islands jsut gonna keep track of the max area of one island

"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            if ( r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            
            return area
              

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area
