"""
import numpy as np

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        
        arr2D = np.array(original).reshape(m, n)
        return arr2D.tolist()

"""
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                res[i][j] = original[i * n + j]
        
        return res

"""
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        
        result = []
        for i in range(m):
            row = original[i * n:(i + 1) * n]
            result.append(row)
        
        return result
        
"""
