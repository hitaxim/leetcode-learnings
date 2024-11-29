class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        #d = Counter(s)
        #n = d[c]
        n = s.count(c)
        return n *(n+1)//2
