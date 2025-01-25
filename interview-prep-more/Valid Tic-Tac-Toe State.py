class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def winning(person, board):
            if person*3 in board or person*3 in ("".join(col) for col in zip(*board)):
                return True
            if board[0][0] == board[1][1] == board[2][2] == person: return True
            if board[0][2] == board[1][1] == board[2][0] == person: return True
        
        x = sum(row.count("X") for row in board)
        o = sum(row.count("O") for row in board)
        if winning("X", board) and winning("O", board): return False
        if winning("X", board) and o + 1 != x: return False
        if winning("O", board) and o != x: return False
        if not 0 <= x - o <= 1: return False
        return True
