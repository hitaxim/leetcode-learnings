class Solution:
    MOD = 10 ** 9 + 7
    
    @staticmethod
    @cache
    def factorial(n):
        if n == 0: 
            return 1
        return n * Solution.factorial(n-1) % Solution.MOD

    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        lengths = [sick[0], n - sick[-1] -1]
        for a, b in pairwise(sick):
            length = b - a - 1
            if length > 0: 
                lengths.append(length)
        
        res = Solution.factorial(sum(lengths))
        for i, x in enumerate(lengths):
            res *= pow(Solution.factorial(x), -1, Solution.MOD)
            res %= Solution.MOD

            if i >= 2: 
                res *= pow(2, x-1, Solution.MOD)
                res %= Solution.MOD
        return res
