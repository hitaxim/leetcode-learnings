class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
      ROWS1, COLS1 = len(grid), len(grid[0])
      ROWS2, COLS2 = ROWS1 * 3, COLS1 * 3
      grid2 = [[0] * COLS2 for _ in range(ROWS2)]

      for r in range(ROWS1):
        for c in range(COLS1):
            r2, c2 = r * 3, c * 3
            if grid[r][c] == "\\":
                grid2[r2][c2] = 1
                grid2[r2 + 1][c2 + 1] = 1
                grid2[r2 + 2][c2 + 2] = 1
            elif grid[r][c] == "/":
                grid2[r2][c2 + 2] = 1
                grid2[r2 + 1][c2 + 1] = 1
                grid2[r2 + 2][c2] = 1

      def dfs(r, c):
        grid2[r][c] = 1
        if r + 1 < len(grid2) and grid2[r + 1][c] == 0:
            dfs(r + 1, c)
        if r - 1 >= 0 and grid2[r - 1][c] == 0:
            dfs(r - 1, c)
        if c + 1 < len(grid2[0]) and grid2[r][c + 1] == 0:
            dfs(r, c + 1)
        if c - 1 >= 0 and grid2[r][c - 1] == 0:
            dfs(r, c - 1)


      count = 0
      for r in range(ROWS2):
        for c in range(COLS2):
            if grid2[r][c] == 0:
                dfs(r, c) 
                count += 1
      return count

"""
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        adj = [[1]*n*3 for _ in range(n*3)]
        for i in range(n):
            for j in range(n):
                r = i*3
                c = j*3
                if grid[i][j]=="/":
                    adj[r+2][c] = 0
                    adj[r+1][c+1] = 0
                    adj[r][c+2] = 0
                elif grid[i][j]=="\\":
                    adj[r][c] = 0
                    adj[r+1][c+1] = 0
                    adj[r+2][c+2] = 0
   
        count = 0
        for i in range(n*3):
            for j in range(n*3):
                if adj[i][j] == 1:
                    self.dfs(adj, i, j)
                    count+=1
        

        return count


    def dfs(self, adj: List[str], i: int, j:int) -> int:
        size = len(adj)
        adj[i][j] = 0
        dir = [[-1,0],[0,-1],[0,1],[1,0]]
        for dx, dy in dir:
            x, y = i + dx, j + dy 

            if(x<0 or x>=size or y<0 or y>=size or adj[x][y]==0):
                continue
            
            self.dfs(adj, x, y)
"""
