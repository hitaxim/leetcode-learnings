class Solution:
   def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
       not_in_2 = []
       not_in_1 = []
       s1, s2 = set(nums1), set(nums2)
       for x in s1:
           if x not in s2:
               if x not in not_in_2:
                   not_in_2.append(x)
       for x in s2:
           if x not in s1:
               if x not in not_in_1:
                   not_in_1.append(x)
       return [not_in_2, not_in_1]
