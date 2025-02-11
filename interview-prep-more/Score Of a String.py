class Solution:
    def scoreOfString(self, s: str) -> int:
        N = len(s)
        total = 0
        for i in range(N-1):
            total += abs(ord(s[i]) - ord(s[i+1]))

        return total
        
