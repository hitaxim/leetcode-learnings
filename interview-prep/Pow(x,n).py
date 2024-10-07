class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calc(x, n):
            if n == 0: 
                return 1
            if n == 1: 
                return x
            res = calc(x, n//2)
            res = res * res
            if n % 2 == 1:
                res = res * x
            return res
        
        ans = calc(x,abs(n))
        if n >= 0: 
            return ans
        else: 
            return 1/ans
