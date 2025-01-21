class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        a=0
        b=-1
        summ=0
        for i in range(len(mat)):
            summ+=(mat[i][a]+mat[i][b] if a!=len(mat)+b else mat[i][a])
            a+=1
            b-=1
        return summ

"""
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        result = 0
        for i in range(n):
            result += mat[i][i] + mat[i][n - i - 1]
        if n % 2 == 1:
            result -= mat[n // 2][n // 2]
        return result
"""
