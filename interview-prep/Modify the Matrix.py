class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ans = matrix.copy()

        for c in range(n):
            max_val = max(matrix[r][c] for r in range(m))
            for r in range(m):
                if matrix[r][c] == -1:
                    ans[r][c] = max_val 

        return ans 
