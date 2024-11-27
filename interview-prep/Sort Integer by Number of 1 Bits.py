class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(sorted(arr), key = lambda x : bin(x).count('1'))
       
