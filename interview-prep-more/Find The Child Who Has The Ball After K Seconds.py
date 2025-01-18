class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        n -= 1
        rounds = k // n
        rem = k % n

        if rounds % 2 == 0:
            return rem
        else:
            return n - rem
        
