class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        if row == 0: 
            return -1

        col = len(grid[0])
        fresh_cnt = 0
        rotten = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    # It is rotten: 
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    fresh_cnt += 1 

        min_pass = 0
        
        while rotten and fresh_cnt > 0: 
            min_pass += 1

            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    xx, yy = x + dx, y + dy

                    if xx < 0 or xx == row or yy < 0 or yy == col: 
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    
                    fresh_cnt -= 1
                    grid[xx][yy] = 2

                    rotten.append((xx,yy))

        return min_pass if fresh_cnt == 0 else -1

"""
2 1 1
1 1 0
0 1 1

2 1 1
0 1 1
1 0 1

0 2 
"""
