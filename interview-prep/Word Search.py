class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def dfs(x, y, k):
            if k == len(word):
                return True
            if x < 0 or x >= row or y < 0 or y>= col or word[k] != board[x][y]:
                return False

            visited = board[x][y]
            board[x][y] = "."
            result = dfs(x+1, y, k+1) or dfs(x, y+1, k+1) or dfs(x-1, y, k+1) or dfs(x, y-1, k+1)
            board[x][y] = visited
            return result
        
        for i in range(row):
            for j in range(col):
                if dfs(i,j,0):
                    return True
        return False
