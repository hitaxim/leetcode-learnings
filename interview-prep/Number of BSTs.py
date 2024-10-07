class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]

        return dp[n]


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.solve(n, dp)

    def solve(self, n, dp):
        if n <= 1: 
            return 1
        if dp[n] != -1: 
            return dp[n]
        ans = 0
        for i in range(1, n+1):
            ans += self.solve(i-1, dp) * self.solve(n-i,dp)
        dp[n] = ans
        return dp[n]

