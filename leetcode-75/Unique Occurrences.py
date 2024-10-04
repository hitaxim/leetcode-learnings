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

#ORRRRRRR

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freqCount = Counter(arr)

        return len(set(freqCount.values())) == len(freqCount)


#ORRRRRR

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ans = {}
        for x in arr:
            if x not in ans:
                ans[x] = 1
            else:
                ans[x] += 1
        if len(ans.values()) == len(set(ans.values())):
            return True
        else :
            return False     
