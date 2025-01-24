"""
class Solution:     
    def countNegatives(self, grid):
        count = 0
        for i in range(len(grid)-1, -1,-1):
            for j in range(len(grid[0])-1,-1, -1):
                if grid[i][j]<0:
                    count +=1
        return(count)
"""

class Solution: 
    def countNegatives(self, grid):
        return sum(a<0 for i in grid for a in i) 
