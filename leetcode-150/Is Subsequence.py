class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #if set(s) not in set(t):
        #    return False
        l_s = 0
        l_t = 0
        while l_s < len(s) and l_t < len(t):
            if s[l_s] == t[l_t]:
                l_s += 1
            l_t += 1
        return l_s == len(s)        
