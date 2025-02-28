def triangular_sum(nums):
  while len(nums) > 1:
    next_n = []
    for i in range(len(nums)- 1):
	    next_n.append((nums[i] + nums[i+1]) % 10)
    nums = next_n
  return nums[0]
