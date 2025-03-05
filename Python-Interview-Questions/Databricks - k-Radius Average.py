def k_radius_avg(nums, k):
    n = len(nums)
   
    averages = [-1] * n
   
    k_radius_size = 2 * k + 1
    
    window_sum = sum(nums[:k_radius_size])
    
    for i in range(k, n - k):
        averages[i] = round(window_sum / k_radius_size, 2)
        if i + k + 1 < n:
            window_sum += nums[i + k + 1] - nums[i - k]
    
    return averages
    
