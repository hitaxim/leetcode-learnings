class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        low = min(a,b,c)
        high = 2*10**9

        def feasible(val):
            result = val//a + val//b + val//c - val//lcm(a,b) - val//lcm(b,c) - val//lcm(a,c) + val//lcm(a,b,c)
            return result>=n
        
        while low<high:
            mid = low+high>>1
            if feasible(mid):
                high = mid
            else:
                low= mid+1
        return low

"""

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # inclusion-exclusion principle
        ab = a*b//gcd(a, b)
        bc = b*c//gcd(b, c)
        ca = c*a//gcd(c, a)
        abc = ab*c//gcd(ab, c)
        
        lo, hi = 1, n*min(a, b, c)
        while lo < hi: 
            mid = lo + hi >> 1
            if mid//a + mid//b + mid//c - mid//ab - mid//bc - mid//ca + mid//abc < n: lo = mid + 1
            else: hi = mid 
        return lo 
"""
