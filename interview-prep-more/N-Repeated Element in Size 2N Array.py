class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        list1 = []
        for i in nums :
            if i in list1 :
                return i
            else :
                list1.append(i)

"""
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        set1 = set()
        for i in nums :
            if i in set1 :
                return i
            else :
                set1.add(i)
"""
