class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        subs = 0
        last_p = [-1] * 3
        for idx in range(len(s)):
            last_p[ord(s[idx]) - ord("a")] = idx
            subs += 1 + min(last_p)
        
        return subs
        
