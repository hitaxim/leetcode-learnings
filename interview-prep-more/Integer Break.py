class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        # Try to divide n into as many threes as possible
        threes = n // 3
        remainder = n % 3

        if remainder == 1:
            threes -= 1 
            remainder = 4 
        elif remainder == 0:
            remainder = 1 

        return (3 ** threes) * remainder
