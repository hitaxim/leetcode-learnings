class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        pdt = 1
        sums = 0
        for i in s: 
            ans = int(i)
            pdt *= ans
            sums += ans
        return pdt - sums
