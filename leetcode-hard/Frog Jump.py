class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {stone : set() for stone in stones}
        dp[0] = {0}

        for stone in stones:
            for jump in dp[stone]:
                for jump_distance in [jump - 1, jump, jump + 1]:
                    # exmaple : jump_distance = 1 and 1 in dp
                    # dp[ 0 + 1].add(1)
                    if jump_distance > 0 and stone + jump_distance in dp:
                        dp[stone + jump_distance].add(jump_distance)
        
        return len(dp[stones[-1]]) > 0
        
