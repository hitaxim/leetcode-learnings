from collections import namedtuple

Directions = namedtuple('Directions', ['x', 'y'])
up = Directions(-1, 0)
down = Directions(1, 0)
left = Directions(0, -1)
right = Directions(0, 1)

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for x, y in guards: 
            matrix[x][y] = 'G'
        for x, y in walls: 
            matrix[x][y] = 'W'
        
        def dfs(row, col, direction):
            if row < 0 or row >= m or col < 0 or col >= n or matrix[row][col] == 'W' or matrix[row][col] == 'G':
                return 
            
            matrix[row][col] = 'X'
            dfs(row + direction.x, col + direction.y, direction)
        
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 'G':
                    dfs(x+1, y, down)
                    dfs(x-1, y, up)
                    dfs(x, y+1, right)
                    dfs(x, y-1, left)
        
        counter = 0
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    counter += 1
        return counter
