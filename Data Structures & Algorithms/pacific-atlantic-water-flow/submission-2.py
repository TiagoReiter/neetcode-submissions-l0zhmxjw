from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        def dfs(r, c, visited, prev_height):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                heights[r][c] < prev_height
            ):
                return

            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])                  # Pacific top
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])   # Atlantic bottom

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])                  # Pacific left
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])   # Atlantic right

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res