class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        c = 0
        while c*k < len(s):
            s = s[:c*k] + s[c*k:c*k+k][::-1] + s[c*k+k:]
            c+=2
        return s

"""
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0,len(s),2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)
"""
