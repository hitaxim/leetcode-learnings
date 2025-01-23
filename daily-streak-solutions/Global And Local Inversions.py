class Solution:
    def isIdealPermutation(self, arr: List[int]) -> bool:
        for ind,val in enumerate(arr):
            if abs(ind-val)>1:
                return False
        return True
