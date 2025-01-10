class Solution:
    def reachNumber(self, target: int) -> int:
        ans, k = 0, 0
        target = abs(target)
        while ans < target:
            ans += k
            k += 1
        while (ans - target) % 2:
            ans += k
            k += 1
        return k - 1  
        
"""
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n, sum_n = 0, 0
        
        while sum_n < target or (sum_n - target) % 2 != 0:
            n += 1
            sum_n += n
            
        return n
"""
