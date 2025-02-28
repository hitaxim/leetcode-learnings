def weakest_strong_link(strength):
	m = len(strength)
	n = len(strength[0])
	
	min_rows = [0] * m 
	max_cols = [0] * n 
	
	for i in range(m):
	  min_rows[i] = min(strength[i])
	 
	for j in range(n):
	  cur_max = 0
	  for i in range(m):
	    cur_max = max(cur_max, strength[i][j])
	  max_cols[j] = cur_max
	
	for i in range(m):
	  for j in range(n):
	    if strength[i][j] == min_rows[i] and strength[i][j] == max_cols[j]:
	      return strength[i][j]
	
	return -1
