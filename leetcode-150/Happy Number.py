class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(n1):
            return sum(int(x)**2 for x in str(n1))

        seen = set()
        while n!= 1 and n not in seen:
            seen.add(n)
            n = next_num(n)

        return n == 1
