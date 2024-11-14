class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)

        while l < r: 
            k = (l + r) // 2
            if sum(ceil(i/k) for i in quantities) <= n :
                r = k
            else: 
                l = k + 1
        return l
