class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m = len(s)
        n = len(g)
        l = r = 0
        g.sort()
        s.sort()

        while l < m and r < n:
            if g[r] <= s[l]:
                r += 1
            l += 1

        return r
