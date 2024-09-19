class Solution:
   def uniqueOccurrences(self, arr: List[int]) -> bool:
       len_arr = len(arr)
       dict_c = {}
       for i in range(len_arr):
           if arr[i] not in dict_c:
               dict_c[arr[i]] = 1
           else:
               dict_c[arr[i]] += 1
       check = set()
       for i in dict_c.values():
           if i in check:
               return False
           check.add(i)
       return True
