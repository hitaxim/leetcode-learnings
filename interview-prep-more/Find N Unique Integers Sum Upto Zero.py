class Solution:
    def sumZero(self, n: int) -> List[int]:
        mass = []
        if n % 2 != 0:
            mass.append(0)
        for i in range(n):
            if len(mass) != n:
                mass.append(-i-1)
                mass.append(i+1)
        return mass
