class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        
        l = len(grid)
        area=0
        for row in range(l):
            for col in range(l):
                if grid[row][col]:
                    area += (grid[row][col]*4) +2 #surface area of each block if blocks werent connected
                if row: #row>0
                    area -= min(grid[row][col],grid[row-1][col])*2 #subtracting as area is common among two blocks
                if col: #col>0
                    area -= min(grid[row][col],grid[row][col-1])*2 #subtracting as area is common among two blocks
        return area

"""
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        
        n = len(grid)

        # outsides
        area = 0
        for i in range(n):
            for j in range(n):
                # upper outside
                if i == 0: area += grid[i][j]
                # left outside
                if j == 0: area += grid[i][j]
                # lower outside
                if i == n-1: area += grid[i][j]
                # right outside
                if j == n-1: area += grid[i][j]
                # lower neighbor delta
                if i+1<n: area += abs(grid[i][j]-grid[i+1][j])
                # right neighbor delta
                if j+1<n: area += abs(grid[i][j]-grid[i][j+1])
                # top/bottom surface
                if grid[i][j]: area += 2

        return area
"""
