class Solution:
   def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
       ans = []
       for i in range(len(nums)):
           if len(ans) >= index[i]:
               ans.insert(index[i], nums[i])
           else:
               ans.append(nums[i])
       return ans
