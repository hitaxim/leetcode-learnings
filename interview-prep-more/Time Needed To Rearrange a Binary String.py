"""
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans = 0
        while '01' in s:
            ans += 1
            s = s.replace('01', '10')
        
        return ans
"""

class Solution: 
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans = prefix = prev = 0 
        for i, ch in enumerate(s): 
            if ch == '1': 
                ans = max(prev, i - prefix)
                prefix += 1
                if ans: prev = ans+1
        return ans 
