def maximumWealth(self, accounts: List[List[int]]) -> int:
        large = 0
        for money in accounts:
            large = max(sum(money), large)
        return large
