class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        if health - grid[0][0] < 1:
            return False
        n, m = len(grid), len(grid[0])
        visited = [[False]*m for _ in range(n)]
        visited[0][0] = True
        q = deque([(health-grid[0][0], 0, 0)])
        while q:
            h, i, j = q.pop()
            if i == n-1 and j == m-1:
                return True
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + dx, j + dy
                if  0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                    if grid[ni][nj]:
                        if h > 1:
                            q.appendleft((h-1, ni, nj))
                            visited[ni][nj] = True
                    else:
                        q.append((h, ni, nj))
                        visited[ni][nj] = True
        return False

"""
class Solution:
    def findSafeWalk(self, grid: List[List[int]], h: int) -> bool:
        m, n = len(grid), len(grid[0])
        vis = [[0 for _ in range(n)] for _ in range(m)]
        memo = {}

        def dfs(x, y, ans):
            if x < 0 or x >= m or y < 0 or y >= n or vis[x][y]== 1 or ans >= h:
                return float('inf')
            
            if x == m-1 and y == n - 1:
                return ans + grid[x][y]
            
            if (x, y, ans) in memo:
                return memo[(x, y, ans)]
            
            vis[x][y] = 1
            memo[(x, y, ans)] = min(dfs(x+1,y,ans+grid[x][y]),dfs(x-1,y,ans+grid[x][y]),dfs(x,y+1,ans+grid[x][y]),dfs(x,y-1,ans+grid[x][y]))
            vis[x][y] = 0
            return memo[(x, y, ans)]
        
        a = dfs(0, 0, 0)
        return a - h < 0

"""
        
