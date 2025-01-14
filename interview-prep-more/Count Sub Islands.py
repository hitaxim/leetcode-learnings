class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        def removeIsland(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid2[x][y] == 0:
                return 
            grid2[x][y] = 0
            for dx, dy in [(0,1), (1, 0), (0 ,-1), (-1, 0)]:
                removeIsland(x + dx, y + dy)

        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    removeIsland(i, j)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    res += 1
                    removeIsland(i, j)
        return res
        
