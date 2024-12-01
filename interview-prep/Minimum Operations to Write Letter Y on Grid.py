class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mid = n // 2
        y_set = set()

        for i in range(mid + 1):
            y_set.add((i,i)) # left diagonal
            y_set.add((i, n - i - 1)) # right
        
        for i in range(mid, n):
            y_set.add((i, mid)) # vertical line down middle
        
        y_vals = [0, 0, 0]
        not_y_vals = [0, 0, 0]

        for i in range(n):
            for j in range(n):
                if (i, j) in y_set:
                    y_vals[grid[i][j]] += 1
                else: 
                    not_y_vals[grid[i][j]] += 1
        
        y_size = len(y_set)
        not_y_size = (n ** 2) - y_size
        min_swap = float('inf')

        for i in range(3):
            for j in range(3):
                if i != j: 
                    swap_to_fix = (y_size - y_vals[i]) + (not_y_size - not_y_vals[j])
                    min_swap = min(min_swap, swap_to_fix)

        return min_swap
