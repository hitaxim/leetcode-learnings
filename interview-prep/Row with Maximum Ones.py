class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ones = 0
        index = 0
        for idx, row in enumerate(mat):
            c = row.count(1)
            if ones < c:
                ones = c
                index = idx
        
        return [index, ones]
        
