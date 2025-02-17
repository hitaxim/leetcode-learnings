class Solution:
    def arrangeCoins(self, n: int) -> int:
        x = int((2*n)**(0.5))
        while x:
            if x*(x+1)//2 <= n:
                return x
            x-=1
