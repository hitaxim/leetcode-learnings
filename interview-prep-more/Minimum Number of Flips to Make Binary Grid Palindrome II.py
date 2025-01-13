class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = single = double = 0

        for i in range(m // 2):
            for j in range(n // 2):
                ones = grid[i][j] + grid[i][n-1-j] + grid[m - 1- i][j] + grid[m - i-1][n-1-j]
                res += min(ones, 4 - ones)
            
            if n % 2 == 1:
                ones = grid[i][n //2] + grid[m-1-i][n//2]
                single += (ones == 1)
                double += (ones == 2)
        
        if m % 2 == 1:
            for j in range(n // 2):
                ones = grid[m //2][j] + grid[m//2][n-1-j]
                single += (ones == 1)
                double += (ones == 2)
            if n % 2 == 1:
                res += grid[m//2][n//2]
        
        if double % 2 == 0 or single > 0:
            return res + single
        return res + 2
        
