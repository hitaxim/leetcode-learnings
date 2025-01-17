class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        
        n = len(colsum)
        matrix = [[0] * n for _ in range(2)]
        if upper + lower != sum(colsum): return []

        for i in range(n):
            if colsum[i] == 2:
                matrix[0][i] = 1
                matrix[1][i] = 1
                upper -= 1
                lower -= 1
            elif colsum[i] == 1:
                if lower <= upper:
                    matrix[0][i] = 1
                    upper -= 1
                else:
                    matrix[1][i] = 1
                    lower -= 1
        
        if upper > 0 or lower > 0:
            return []
        
        return matrix
