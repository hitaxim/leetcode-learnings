class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            result.append(total)
        return result

"""
def runningSum(self, nums: List[int]) -> List[int]:
	result = []
	result.append(nums[0])
	for i in range(1, len(nums)):
		result.append(result[-1]+nums[i])
	return result
""" 
