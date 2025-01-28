class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(r):
            if r == n:
                copy = board[:]
                sol = []
                for c in copy:
                    sol.append("".join(c[:]))
                ans.append(sol)
                return

            for c in range(n):
                if c in placedCol or r + c in placedPos or r - c in placedNeg: continue

                board[r][c] = "Q"
                placedCol.add(c)
                placedPos.add(r + c)
                placedNeg.add(r - c)

                backtrack(r + 1)

                board[r][c] = "."
                placedCol.remove(c)
                placedPos.remove(r + c)
                placedNeg.remove(r - c)

        board = [["."] * n for _ in range(n)]
        
        placedCol = set()
        placedPos = set()
        placedNeg = set()
        ans = []
        backtrack(0)
        return ans

"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        if n == 2 or n == 3:
            return []

        results = []
        solution = [-1] * n
        self.solveNQueensRec(n, solution, 0, results)
        return results

    def solveNQueensRec(
        self, n: int, solution: List[int], row: int, results: List[List[str]]
    ):
        if row == n:
            results.append(self.constructSolutionString(solution))
            return

        for col in range(n):
            if self.isValidMove(row, col, solution):
                solution[row] = col
                self.solveNQueensRec(n, solution, row + 1, results)
                solution[row] = -1  # Backtrack

    def isValidMove(
        self, proposedRow: int, proposedCol: int, solution: List[int]
    ) -> bool:
        for i in range(proposedRow):
            oldRow = i
            oldCol = solution[i]
            diagonalOffset = proposedRow - oldRow

            if (
                oldCol == proposedCol
                or oldCol == proposedCol - diagonalOffset
                or oldCol == proposedCol + diagonalOffset
            ):
                return False
        return True

    def constructSolutionString(self, solution: List[int]) -> List[str]:
        board = []
        for row in range(len(solution)):
            row_str = ["."] * len(solution)
            row_str[solution[row]] = "Q"
            board.append("".join(row_str))
        return board
"""
