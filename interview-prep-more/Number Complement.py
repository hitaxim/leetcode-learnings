class Solution:
    def findComplement(self, num: int) -> int:
        bit_len = num.bit_length()

        mask = (1 << bit_len) - 1
        return num ^ mask 

"""
class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        flipped = ''.join('1' if b == '0' else '0' for b in binary)
        return int(flipped, 2)
"""

"""
class Solution:
    def findComplement(self, num: int) -> int:
        xor = 1
        for i in range(len(bin(num)) - 2):
            num ^= xor
            xor <<= 1
        return num
"""
