def two_sum(nums: list[int], target: int) -> list[int]:
    for idx, num in enumerate(nums):
      if (target - num) in nums and num != (target-num):
        return [idx, nums.index(target - num)]
    return [-1, -1]

"""
def two_sum(nums: list[int], target) -> list[int]:
    d = {}
    for i in range(len(nums)):
        cur_value = nums[i]
        complement = target - cur_value
        if complement in d:
            return [d[complement], i]
        d[cur_value] = i
    
    return [-1, -1]
"""
