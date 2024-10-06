class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        def zero(i,j):

            if (i!=m and i!=-1 and j!=n and j!=-1 and  grid[i][j]=="1"):
                grid[i][j]="0"
                zero(i+1,j)
                zero(i-1,j)
                zero(i,j+1)
                zero(i,j-1)
            
            return

        total =0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    total+=1
                    zero(i,j)

        return total   


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands
