class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        def primes(n) -> int:

            if n %2 == 0: self.ans|= (1 << 2)
            while n %2 == 0: n//= 2

            for p in range(3, isqrt(n) + 1, 2):
                if  n == 1: break

                if n %p == 0: self.ans|= (1 << p)
                while n %p == 0: n//= p

            if  n > 1: self.ans|= (1 << n)
            return 

        self.ans = 0
        for n in nums: primes(n)
        return self.ans.bit_count()                    
