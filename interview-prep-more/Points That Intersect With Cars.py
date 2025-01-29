class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        s = set()
        for st, end in nums:
            s|= set(range(start,end+1))
        return len(s)
        

"""
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        return len(set(j for i in nums for j in range(i[0], i[1] + 1)))
"""
