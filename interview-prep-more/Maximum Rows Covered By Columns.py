"""
from itertools import combinations
class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        rows = 0
        for c in combinations(range(len(mat[0])), cols):
            temp = 0
            for r in mat:
                valid = True
                for col, n in enumerate(r):
                    if valif and n == 1 and col not in c:
                        valid = False
                if valid:
                    temp += 1
            
            rows = max(rows, temp)
        
        return rows

"""

class Solution:
    def maximumRows(self, m: List[List[int]], k: int) -> int:
        n = len(m[0])
        result = 0
        for q in combinations([*range(n)], n-k):
            res = 0
            for r in m:
                res += all(r[c] == 0 for c in q)

            result = max(result, res)
        
        return result
