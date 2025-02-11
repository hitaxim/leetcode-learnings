"""
class Solution:
    def countPrimes(self, n: int) -> int:

        arr = [True] * n

        if n == 0 or n == 1:
            return 0

        arr[0], arr[1] = False, False

        for i in range(2, int(n ** 0.5) + 1):
            if arr[i]:
                for j in range(i + i, n, i):
                    arr[j] = False

        return sum(arr)  
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                is_prime[p * p:n:p] = [False] * ((n - 1 - p * p) // p + 1)
        return sum(is_prime)
        
