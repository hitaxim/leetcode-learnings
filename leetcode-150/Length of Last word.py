class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        m = s.strip().split()

        if not m: 
            return 0
        return len(m[-1])        
        
