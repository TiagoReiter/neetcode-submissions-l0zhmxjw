"""
Restate: I need to find all connected ones tha from an island.
Thoughts:
1. The number of islands depends on if the 1 clusters are connected or not
2. As soon as we reach a one we can set it to zero and explore the other directions
3. Directions wise we can go in 4 differenst driectipns up down left right. 
4. Egdge Cases: Reaching end of row, column or a zero

Approach:
1. Define the directions
2. Define a dfs function
3. In that 

"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions  = [[1,0],[-1, 0], [0, 1], [0, -1]]
        islands = 0
        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] == "0"):
                return 
            
            grid[r][c] = "0"

            for dr, dc in directions:
                dfs(r + dr, c+dc)
            
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands