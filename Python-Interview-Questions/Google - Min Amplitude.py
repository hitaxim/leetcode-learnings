
def min_amplitude(arr):
    
    if len(arr) < 5:
        return 0
    
    arr.sort()
    
   
    case_1 = arr[-1] - arr[3]
 
    case_2 = arr[-2] - arr[2]  
  
    case_3 = arr[-3] - arr[1]  
   
    case_4 = arr[-4] - arr[0]  

    # Return the smallest amplitude from the four cases
    return min(case_1, case_2, case_3, case_4)
    
