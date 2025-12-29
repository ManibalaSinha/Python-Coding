from typing import List

def numIslands(grid: List[List[str]]) -> int:
    if not grid: 
        return 0
    
    rows, cols = len(grid), len(grid[0])
    
    def dfs(r, c):
        # boundary check + water check
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
            return
        # mark as visited
        grid[r][c] = "0"
        # explore neighbors
        dfs(r+1, c)  # down
        dfs(r-1, c)  # up
        dfs(r, c+1)  # right
        dfs(r, c-1)  # left
    
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)  # mark whole island
    return count
grid1 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid1)) 