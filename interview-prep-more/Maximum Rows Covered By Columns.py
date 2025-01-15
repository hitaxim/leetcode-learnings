
from itertools import combinations
class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        rows = 0
        for c in combinations(range(len(matrix[0])), numSelect):
            temp = 0
            for r in matrix:
                valid = True
                for col, n in enumerate(r):
                    if valid and n == 1 and col not in c:
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
"""
