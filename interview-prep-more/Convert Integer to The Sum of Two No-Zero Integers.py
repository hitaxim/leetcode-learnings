"""
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            for j in range(n):
                if i + j == n and i != 0 and j != 0 and "0" not in str(i) and "0" not in str(j):
                    return [i,j]

"""
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n):
            if "0" not in (str(n-i)) and "0" not in str(i):
                return [i,n-i]
  
