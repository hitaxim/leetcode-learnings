def max_avg_subarray(nums, k):
   
    current_sum = sum(nums[:k])
    max_sum = current_sum
    
 
    for i in range(k, len(nums)):
   
        current_sum += nums[i] - nums[i - k]
      
        max_sum = max(max_sum, current_sum)

    return round(max_sum / k, 2)
    
