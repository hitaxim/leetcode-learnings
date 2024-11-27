class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_count = [0] * m
        column_count = [0] * n
        
        for row, column in indices:
            row_count[row] += 1
            column_count[column] += 1
        
        odd_count = 0
        for row_index in range(m):
            for column_index in range(n):
                if (row_count[row_index] + column_count[column_index]) % 2 != 0:
                    odd_count += 1
        
        return odd_count

"""
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(len(indices)):
            a = indices[i][0]
            b = indices[i][1]
            for j in range(n):
                mat[a][j] += 1
            for k in range(m):
                mat[k][b] += 1
        c = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] % 2:
                    c += 1
        return c
"""
