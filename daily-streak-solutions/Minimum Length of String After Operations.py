class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(1 if freq % 2 else 2 for freq in Counter(s).values())
    
"""
from collections import defaultdict

class Solution:
    def minimumLength(self, s: str) -> int:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        res = 0
        for _, val in counter.items():
            if val <= 2:
                res += val
            else:
                if val & 1 == 0:
                    res += 2
                else:
                    res += 1
        return res
            
        
"""
        
