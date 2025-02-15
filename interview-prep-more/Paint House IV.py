class Solution:
    def __init__(self):
        self.dp = None

    def solve(self, c, l, r, i):
        n = len(c)
        if i >= n // 2:
            return 0

        if self.dp[i][l][r] != -1:
            return self.dp[i][l][r]

        left_choices = [j for j in range(3) if j != l]
        right_choices = [j for j in range(3) if j != r]

        ans = float('inf')

        for h in left_choices:
            for j in right_choices:
                if h == j:
                    continue
                cl = c[i][h]
                cr = c[n - i - 1][j]
                ans = min(ans, cl + cr + self.solve(c, h, j, i + 1))

        self.dp[i][l][r] = ans
        return ans

    def minCost(self, n, c):
        self.dp = [[[-1] * 4 for _ in range(4)] for _ in range(n // 2 + 1)]
        return self.solve(c, 3, 3, 0)

"""
class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        dp = [0] * 6
        for i in range(n >> 1):
            dp = [
                cost[i][0] + cost[n - i - 1][1] + min(dp[2:5]),
                cost[i][0] + cost[n - i - 1][2] + min([dp[2]] + dp[4:]),
                cost[i][1] + cost[n - i - 1][0] + min(dp[:2] + [dp[5]]),
                cost[i][1] + cost[n - i - 1][2] + min([dp[0]] + dp[4:]),
                cost[i][2] + cost[n - i - 1][0] + min(dp[:2] + [dp[3]]),
                cost[i][2] + cost[n - i - 1][1] + min(dp[1:4]),
            ]
        return min(dp)

class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        n = len(cost)
        ncost = []
        for i in range(n // 2):
            ncost.append([cost[i], cost[n - i - 1]])
        cost = ncost

        n = n // 2

        @cache
        def recur(i, a, b):
            if i == n:
                return 0

            ans = 999999999999
            for x in range(3):
                for y in range(3):
                    if x != a and y != b and x != y:
                        ans = min(ans, cost[i][0][x] + cost[i][1][y] + recur(i + 1, x, y))
            return ans

        return recur(0, -1, -1)
"""
