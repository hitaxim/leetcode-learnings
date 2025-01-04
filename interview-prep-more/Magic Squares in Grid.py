class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                # Extract the 3x3 grid
                square = [grid[i][j], grid[i][j+1], grid[i][j+2],
                          grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                          grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]]

                # Check if the square contains all numbers 1 through 9
                if set(square) == set(range(1, 10)):
                    # Check if the sums of rows, columns, and diagonals are equal
                    if (sum(grid[i][j:j+3]) == sum(grid[i+1][j:j+3]) == sum(grid[i+2][j:j+3]) == 
                        sum([grid[i][j], grid[i+1][j], grid[i+2][j]]) ==
                        sum([grid[i][j+1], grid[i+1][j+1], grid[i+2][j+1]]) == 
                        sum([grid[i][j+2], grid[i+1][j+2], grid[i+2][j+2]]) ==
                        sum([grid[i][j], grid[i+1][j+1], grid[i+2][j+2]]) ==
                        sum([grid[i][j+2], grid[i+1][j+1], grid[i+2][j]])):
                        count += 1

        return count
