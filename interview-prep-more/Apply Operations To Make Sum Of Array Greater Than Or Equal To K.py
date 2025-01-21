class Solution:
    def minOperations(self, k: int) -> int:
        p = isqrt(k)
        q = (k+p-1)//p
        return p+q-2


"""
class Solution:
    def minOperations(self, k: int) -> int:
        res = k+1
        for i in range(1,k+1):
            curr = i-1+(k+i-1) // i-1
            res = min(res,curr)
        return res
"""
