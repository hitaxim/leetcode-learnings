def gpu_idle_days(days, training_sessions):
    # Step 1: Sort the intervals
    training_sessions.sort()
    
    # Step 2: Merge overlapping intervals while counting days
    total_used_days = 0
    start, end = training_sessions[0]
    
    for s, e in training_sessions:
        if start <= s <= end:  # Overlap detected
            end = max(end, e)  # Merge by extending the interval
        else:
        	# Add the current interval's days
            total_used_days += (end - start + 1)  
            start, end = s, e
   
    # Add the last interval
    total_used_days += (end - start + 1)
    
    return days - total_used_days
    
