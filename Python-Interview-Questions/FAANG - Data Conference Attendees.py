def min_attendees(answers):
    frequency = {}
    res = 0
    
    for ans in answers:
        # Initialize the count for each new answer
        if ans not in frequency:
            frequency[ans] = 0
        
        # If a new batch is needed, add it to the result
        if frequency[ans] % (ans + 1) == 0:
            res += ans + 1
        
        # Update the count for the current answer
        frequency[ans] += 1
    
    return res
    
