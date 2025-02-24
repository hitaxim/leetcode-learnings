class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        res = 0
        for i in range(L, R+1):
            bits = bin(i).count('1')
            if bits != 1 and math.factorial(bits - 1)  % bits == bits - 1:
                res += 1
        return res 

"""
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0

        for num in range(left, right+1):

            set_bits = num.bit_count()

            if set_bits in primes:
                count += 1

        return count
"""
