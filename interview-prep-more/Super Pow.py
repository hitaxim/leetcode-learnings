class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        p = ''
        for i in b:
            p+=str(i)
        p=int(p)
        return pow(a,p,mod)

"""
mod = 1337
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        ans = 1
        i = len(b) - 1
        y = a
        while i >= 0:
            ans = (ans * pow(y, b[i], mod)) % mod
            y = pow(y, 10, mod)
            i -= 1
        return ans
"""
