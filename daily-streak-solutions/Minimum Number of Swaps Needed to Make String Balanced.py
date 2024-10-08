class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        for char in s: 
            if char =="[":
                ans += 1
            elif ans > 0: 
                ans -= 1
        return (ans + 1)//2
    
    """
        p = 0
        for c in s: 
            p = max(0, p+(c==']')-(c=="]"))
        return (p+1)//2
    """
        
