def rotate(matrix):
  # Transpose
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
   # Reverse rows
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
    return matrix
