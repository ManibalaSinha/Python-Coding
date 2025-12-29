from collections import deque

def shortestBridge(grid):
    n = len(grid)
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[0]*n for _ in range(n)]
    q = deque()

    # DFS to mark first island
    def dfs(r,c):
        if (r<0 or c<0 or r>=n or c>=n or 
            visited[r][c] or grid[r][c]==0):
            return
        visited[r][c] = 1
        q.append((r,c,0))  # start BFS from island 1
        for dr,dc in directions:
            dfs(r+dr,c+dc)

    # find first island
    found = False
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i,j)
                found = True
                break
        if found: break

    # BFS expansion until hitting 2nd island
    while q:
        r,c,d = q.popleft()
        for dr,dc in directions:
            nr,nc = r+dr,c+dc
            if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
                if grid[nr][nc] == 1:  # found other island
                    return d
                visited[nr][nc] = 1
                q.append((nr,nc,d+1))
grid = [
  [0,1,0],
  [0,0,0],
  [0,0,1]
]
print(shortestBridge(grid))