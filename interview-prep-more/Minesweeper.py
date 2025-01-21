class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        m = len(board)
        n = len(board[0])
        q = deque()
        q.append(click)
        visited = set()
        visited.add(tuple(click))
        while q:
            # print(q)
            for _ in range(len(q)):
                curr = q.popleft()
                x, y = curr[0], curr[1]
                
                
                count_mine = 0
                for a,b in [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(-1,1),(1,1),(1,-1)]:
                    nx, ny = x+a, y+b

                    if 0 <= nx < m and 0 <= ny < n:
                        if board[nx][ny] == 'M':
                            count_mine += 1
                if count_mine > 0:
                    board[x][y] = str(count_mine)
                else:
                    board[x][y] = 'B'
                    for a, b in [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(-1,1),(1,1),(1,-1)]:
                        nx, ny = x+a, y+b

                        if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited:
                            q.append([nx,ny])
                            visited.add((nx,ny))
        return board

"""
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
       # Recursive Approach: DFS
        
        if not board:
            return board

        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        ROWS, COLS = len(board), len(board[0])
        CLICK_R, CLICK_C = click 

        def count_mines(row, col):
            count = 0
            for dr, dc in DIRECTIONS:
                new_r, new_c = row + dr, col + dc
                if (0 <= new_r < ROWS and 0 <= new_c < COLS and board[new_r][new_c] == 'M'):
                    count += 1
            return count

        def explore_cell(row, col):
            adj_mines = count_mines(row, col)

            if adj_mines > 0:
                board[row][col] = str(adj_mines)
            else:
                board[row][col] = 'B'
                for dr, dc in DIRECTIONS:
                    new_r, new_c = row + dr, col + dc
                    if (0 <= new_r < ROWS and 0 <= new_c < COLS and board[new_r][new_c] == 'E'):
                        explore_cell(new_r, new_c)

        if board[CLICK_R][CLICK_C] == 'M':
            board[CLICK_R][CLICK_C] = 'X'
        else:
            explore_cell(CLICK_R, CLICK_C) # Click on 'E'
        
        return board

        # O(m * n) time.
        # O(m * n) auxiliary space.
        # O(m * n) total space.
"""
