"""
def max_three(input):
	max_p = input[0] * input[1] * input[2]
	for i in range(len(input)- 2):
	  for j in range(i+1, len(input)-1):
	    for k in range(j+1, len(input)):
	      cur_p = input[i] * input[j] * input[k]
	      if cur_p > max_p:
	        max_p = cur_p
	return max_p

"""
import heapq

def max_three(input):
	a = heapq.nlargest(3, input) # largest 3 numbers 
	b = heapq.nsmallest(2, input) # smallest 2 (for negatives case) 
	return max(a[2]*a[1]*a[0], b[1]*b[0]*a[0]) # compare
	
