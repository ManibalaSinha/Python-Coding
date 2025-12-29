from collections import deque

def shortestBridge(grid):
    n = len(grid)
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    
    def dfs(i, j):
        if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] != 1:
            return
        grid[i][j] = 2
        q.append((i, j, 0))
        for dx, dy in dirs:
            dfs(i+dx, j+dy)
    
    q = deque()
    found = False
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j)
                found = True
                break
        if found: break
    
    while q:
        i, j, d = q.popleft()
        for dx, dy in dirs:
            x, y = i+dx, j+dy
            if 0 <= x < n and 0 <= y < n:
                if grid[x][y] == 1:
                    return d
                if grid[x][y] == 0:
                    grid[x][y] = 2
                    q.append((x, y, d+1))
grid = [
 [0,1],
 [1,0]
]
print(shortestBridge(grid))