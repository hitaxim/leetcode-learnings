class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        result = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                total_sum = 0
                count = 0

                for x in range(max(0, i-1), min(rows, i+2)):
                    for y in range(max(0, j-1), min(cols, j+2)):
                        total_sum += img[x][y]
                        count += 1

                result[i][j] = total_sum // count

        return result

"""
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),  (0, 0),  (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
    
        for i in range(m):
            for j in range(n):
                total, count = 0, 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        total += img[ni][nj]
                        count += 1
                result[i][j] = total // count
        return result
"""
