class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        k = 0
        for i in range(len(grid)):
            a = []
            for j in range(len(grid)):
                a.append(grid[j][i])
            if a in grid:
                k+=grid.count(a)
        return k


ORRRRRRR

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        val = 0
        for i in range(n):
            row = ",".join(map(str, grid[i]))
            for j in range(n):
                col = ",".join(str(grid[k][j]) for k in range(n))
                if row == col: 
                    val +=1
        return val
