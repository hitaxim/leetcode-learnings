class Solution:
    def countServers(self, g: List[List[int]]) -> int:
        rows, cols = len(g), len(g[1])

        row = [0] * rows
        col = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if g[i][j] :
                    row[i] += 1
                    col[j] += 1

        count = 0
        for i in range(rows):
            for j in range(cols):
                if (g[i][j] == 1 and (col[j] > 1 or row[i] > 1)) :
                    count += 1

        return count     
