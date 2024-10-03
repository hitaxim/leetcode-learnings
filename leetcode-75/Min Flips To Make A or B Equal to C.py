# 
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        operations = 0
        while a > 0 or b > 0 or c > 0: 
            if c & 1:  # If c has 1 in unit 
                if not (a & 1 or b & 1): # A or B doesn't
                    operations += 1
            else: 
                if a & 1: 
                    operations += 1
                if b & 1: 
                    operations += 1
            
            a >>= 1
            b >>= 1
            c >>= 1
        return operations
