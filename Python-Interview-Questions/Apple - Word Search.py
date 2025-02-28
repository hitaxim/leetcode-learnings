def exist(board, word):

  M_ROWS = len(board)
  N_COLS = len(board[0])

  def search(i,j,word_pos):
    """
    Check if possible to find word[word_pos:]
    from location (i,j) on current board
    """
  
    # BASE CASE -- reached end of word
    if word_pos == len(word):
      return True
  
    # RECURSION -- True if word[word_pos] matches and
    # can get word[word_pos+1:] from at least one neighbor
  
    # verify (i,j) is in bounds and current letter matches
    if (
      0 <= i < M_ROWS and 0 <= j < N_COLS 
      and board[i][j] == word[word_pos]
    ):
      board[i][j] = '.'
      # can get word[word_pos+1:] from at least one neighbor?
      if (
        search(i+1, j, word_pos+1)    # down
        or search(i-1, j, word_pos+1) # up
        or search(i, j+1, word_pos+1) # right
        or search(i, j-1, word_pos+1) # left
        ):
        return True
      board[i][j] = word[word_pos]
  
    return False

  # start search from each position on the board
  for i in range(M_ROWS):
    for j in range(N_COLS):
      if search(i,j,0):
        return True
  return False
