class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        dp = [0] * (len(pressedKeys)+ 1)
        dp[0] = 1
        for i, ch in enumerate(pressedKeys):
            dp[i+1] = dp[i]
            if i and pressedKeys[i-1] == ch:
                dp[i+1] += dp[i-1]
                if i >= 2 and pressedKeys[i-2] == ch: 
                    dp[i+1] += dp[i-2]
                    if i >= 3 and pressedKeys[i-3] == ch and ch in "79": dp[i+1] += dp[i-3]
            dp[i+1] %= 1_000_000_007
        return dp[-1]
