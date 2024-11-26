class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        a = n - n//2
        b = n // 2
        c = m - m // 2
        d = m // 2
        a *= d
        b *= c
        return a + b
