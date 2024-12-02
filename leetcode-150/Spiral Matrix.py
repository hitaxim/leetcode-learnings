class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])

        row, col = 0, -1
        direction = 1

        ans = []

        while rows > 0 and cols > 0: 
            # left to right (if direction == 1)
            # right to left (if direction == -1)
            for _ in range(cols):
                col += direction 
                ans.append(matrix[row][col])
            rows -= 1

            for _ in range(rows):
                row += direction 
                ans.append(matrix[row][col])
            cols -= 1
        
            direction *= -1
        
        return ans
