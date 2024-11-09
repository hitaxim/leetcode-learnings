class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        n = len(grid[0])
        for i in range(len(grid)-2, -1 ,-1):
            for j in range(n):
                grid[i][j] += min([moveCost[grid[i][j]][cols] + grid[i+1][cols] for cols in range(n)])
        return min(grid[0])
