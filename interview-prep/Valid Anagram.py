class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        if set(s) != set(t):
            return False

        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)): 
            if t[i] != s[i]:
                return False
        return True 
