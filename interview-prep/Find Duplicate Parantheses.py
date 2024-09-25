def findDuplicateparenthesis(string): 
	Stack = [] 
	for ch in string:
		if ch == ')': 
		
			top = Stack.pop() 
			
			elementsInside = 0
			while top != '(': 
			
				elementsInside += 1
				top = Stack.pop() 
			
			if elementsInside < 1: 
				return True

		# push open parenthesis '(', operators 
		# and operands to stack 
		else:
			Stack.append(ch) 
	
	# No duplicates found 
	return False

# Driver Code
if __name__ == "__main__": 

	# input balanced expression 
	string = "(((a+(b))+(c+d)))"

	if findDuplicateparenthesis(string) == True: 
		print("Duplicate Found") 
	else:
		print("No Duplicates Found") 
