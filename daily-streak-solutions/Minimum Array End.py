class Solution:
    def minEnd(self, n: int, x: int) -> int:
        num = n-1
        ans = 0
        pow = 0
        while num > 0 or x > 0:
            lb = num & 1
            while x & 1:
                ans += 2**pow
                x >>= 1
                pow += 1
            ans += 2**pow * lb
            num >>= 1
            x >>= 1
            pow += 1
        return ans
