def is_same_stripes(matrix):
	diagonals = {}
	
	for i in range(len(matrix)):
	  for j in range(len(matrix[0])):
	    if i-j in diagonals and diagonals[i-j] != matrix[i][j]:
	      return False
	    else: 
	      diagonals[i-j] = matrix[i][j]
	      
	return True
   
