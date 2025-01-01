class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        dp = [[[0, 0] for _ in range(one+1)] for _ in range(zero+1)]
        MOD = 10 ** 9 + 7
        for i in range(min(zero, limit) + 1):
            dp[i][0] = [1, 0]
        for j in range(min(one, limit) + 1):
            dp[0][j] = [0, 1]
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][1]
                dp[i][j][1] = dp[i][j - 1][0] + dp[i][j - 1][1]
                if i > limit:
                    dp[i][j][0] -= dp[i - limit - 1][j][1]
                if j > limit:
                    dp[i][j][1] -= dp[i][j - limit - 1][0]
                dp[i][j][0] %= MOD
                dp[i][j][1] %= MOD
        return (dp[-1][-1][0] + dp[-1][-1][1]) % MOD
                  

"""
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mo = (10**9)+7
        store = [[[0,0] for _ in range(one+1)] for _ in range(zero+1)]
        for i in range(zero+1):
            store[i][0] = [1,0] if i<=limit else [0,0]
        for j in range(one+1):
            store[0][j] = [0,1] if j<=limit else [0,0]
        for i in range(1,zero+1):
            for j in range(1,one+1):
                store[i][j]=[sum(store[i-1][j]),sum(store[i][j-1])]
                if i>limit:
                    store[i][j][0]-=store[i-limit-1][j][1]
                if j>limit:
                    store[i][j][1]-=store[i][j-limit-1][0]
                for t in range(2):
                    store[i][j][t]%=mo
        return sum(store[-1][-1])%mo
"""
