class Solution:
    def minOperations(self, n: int) -> int:

        pows = [1 << i for i in range(int(log2(n))+2)]
        ops = 0

        while n:
            closest = min(pows, key=lambda p: abs(n-p))
            n = abs(n-closest)
            ops += 1

        return ops
