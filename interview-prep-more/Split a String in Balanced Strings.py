class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        for c in s:
            if c == 'R': r += 1
            if c == 'L': l += 1
            if l == r: res += 1
        return res
