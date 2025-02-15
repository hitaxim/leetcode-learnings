class Solution:
    def sortMatrix(self, matrix):
        # Dictionary to store diagonals, where key is the difference of row and column index
        diagonal_map = {}
        rows, cols = len(matrix), len(matrix[0])

        # Traverse the matrix and group elements by their diagonal (row - col)
        for i in range(rows):
            for j in range(cols):
                key = i - j
                if key not in diagonal_map:
                    diagonal_map[key] = []
                diagonal_map[key].append(matrix[i][j])

        # Sort each diagonal: negative keys (upper diagonals) in ascending order,
        # positive keys (lower diagonals) in descending order
        for key in diagonal_map:
            if key < 0:
                diagonal_map[key].sort()
            else:
                diagonal_map[key].sort(reverse=True)

        # Populate the sorted values back into the matrix
        for i in range(rows):
            for j in range(cols):
                key = i - j
                matrix[i][j] = diagonal_map[key].pop(0)

        return matrix

"""
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        starts = []

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    starts.append([r, c, ])


        for row, col in starts:
            r, c = row, col
            temp = []
            while r < ROWS and c < COLS:
                temp.append(grid[r][c])
                r += 1
                c += 1

            temp.sort()
            r, c = row, col
            di = 1 if col else -1
            i = 0 if col else len(temp) - 1
            while r < ROWS and c < COLS:
                grid[r][c] = temp[i]
                i += di
                r += 1
                c += 1

        return grid
                    
"""
