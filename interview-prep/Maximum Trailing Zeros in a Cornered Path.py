class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        def factors(num):
            res = [0,0]
            while num > 1 and num%2 == 0:
                num //= 2
                res[0] += 1
            while num > 1 and num%5 == 0:
                num //= 5
                res[1] += 1
            return res
        def zeros(a, b, c):
            return min(a[0]+b[0]-c[0], a[1]+b[1]-c[1])
        m, n = len(grid), len(grid[0])
        UD = [[0 for i in range(n)] for _ in range(m)]
        LR = [[0 for i in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                UD[i][j] = factors(grid[i][j])
                LR[i][j] = factors(grid[i][j])
                UD[i][j][0] += UD[i-1][j][0] if i else 0
                UD[i][j][1] += UD[i-1][j][1] if i else 0
                LR[i][j][0] += LR[i][j-1][0] if j else 0
                LR[i][j][1] += LR[i][j-1][1] if j else 0
        DU = [[0 for i in range(n)] for _ in range(m)]
        RL = [[0 for i in range(n)] for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                DU[i][j] = factors(grid[i][j])
                RL[i][j] = factors(grid[i][j])
                DU[i][j][0] += DU[i+1][j][0] if i < m - 1 else 0
                DU[i][j][1] += DU[i+1][j][1] if i < m - 1 else 0
                RL[i][j][0] += RL[i][j+1][0] if j < n - 1 else 0
                RL[i][j][1] += RL[i][j+1][1] if j < n - 1 else 0
        res = 0
        for i in range(m):
            for j in range(n):
                f = factors(grid[i][j])
                cur = max(zeros(UD[i][j],LR[i][j],f), zeros(UD[i][j],RL[i][j],f), zeros(DU[i][j],LR[i][j],f), zeros(DU[i][j],RL[i][j],f))
                res = max(res, cur)
        return res
                
        
