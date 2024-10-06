class Solution:
   def removeDuplicates(self, nums: List[int]) -> int:
       index = 0
       dict_a = {}

       for i in range(len(nums)):
           dict_a[nums[i]] = dict_a.get(nums[i], 0) + 1
           if dict_a[nums[i]] <= 2:
               nums[index] = nums[i]
               index += 1
       return index



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[pos - 2]:
                nums[pos] = nums[i]
                pos += 1
        return pos 
        
