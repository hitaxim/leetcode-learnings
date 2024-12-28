"""
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
      nums.sort()
      pos=heapq.nlargest(3,nums)
      neg=heapq.nsmallest(2,nums)
      return max(neg[0]*neg[1]*pos[0],pos[-1]*pos[-2]*pos[-3])

"""


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
