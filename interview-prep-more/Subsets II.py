class Solution:
    def subsetsWithDup(self, nums):
        result = []
        nums.sort()  

        def _backtrack(i, arr, res):

            
            res.append(arr[:])
               
            
            for j in range(i,len(nums)):

                if j > i and nums[j] == nums[j-1]:
                    continue

                arr.append(nums[j])
                _backtrack(j+1, arr , res)
                arr.pop()


        _backtrack(0, [], result)
        return result

"""
class Solution:
  def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
    ans = []
    def dfs(s: int, path: list[int]) -> None:
      ans.append(path)
      if s == len(nums):
        return

      for i in range(s, len(nums)):
        if i > s and nums[i] == nums[i - 1]:
          continue
        dfs(i + 1, path + [nums[i]])

    nums.sort()
    dfs(0, [])
    return ans
"""
