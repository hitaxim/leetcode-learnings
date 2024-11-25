from collections import deque

class Solution:
    def slidingPuzzle(self, board):
        dr = [0, 1, 0, -1]
        dc = [-1, 0, 1, 0]
        target = [[1, 2, 3], [4, 5, 0]]

        # Find position of empty cell (0)
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    r, c = i, j

        queue = deque([(r, c, board, 0)])
        visited = set()
        visited.add(str(board))

        # BFS loop
        while queue:
            row, col, curr_board, steps = queue.popleft()
            if curr_board == target:
                return steps

            for i in range(4):
                new_row, new_col = row + dr[i], col + dc[i]
                if 0 <= new_row < 2 and 0 <= new_col < 3:
                    new_board = [row[:] for row in curr_board]
                    new_board[row][col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[row][col]

                    board_str = str(new_board)
                    if board_str not in visited:
                        queue.append((new_row, new_col, new_board, steps + 1))
                        visited.add(board_str)

        return -1
