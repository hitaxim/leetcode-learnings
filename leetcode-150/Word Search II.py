def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    
    def exist(word: str) -> bool:
        if len(word) > len(board[0]) * len(board):
            return False
        
        def backtracking(i, j, word_idx: int) -> bool:
            if word_idx == len(word):
                return True
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0])
                return False # went out of borders

            elif board[i][j] != word[word_idx]:
                return False # current letter does not match
            
            buff, board[i][j] = board[i][j], '#'
            res = (
                backtracking(i + 1, j, word_idx + 1) or
                backtracking(i - 1, j, word_idx + 1) or
                backtracking(i, j + 1, word_idx + 1) or
                backtracking(i, j - 1, word_idx + 1)
            )

            board[i][j] = buff
            return res
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtracking(i, j, 0):
                    return True
        return False

    res = []

    for word in words:
        if exist(word):
            res.append(word)
    return res
