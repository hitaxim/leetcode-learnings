class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       dict_ans = {}

       for i, x in enumerate(nums):
            left = target - x

            if left in dict_ans: 
                return [i, dict_ans[left]]

            dict_ans[x] = i
