class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        cur = [0] * C
        result = 0
        for r in grid:
            sm = 0
            for i in range(C):
                sm += r[i]
                cur[i] += sm
                result += cur[i] <= k

            if cur[0] > k:
                break

        return result
