class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        #return any(target in row for row in matrix)
        m=len(mat)
        n=len(mat[0])
        
        i=m-1
        j=0
        
        while i>=0 and j<n:
            if mat[i][j]==target:
                return True
            elif mat[i][j]<target:
                j+=1
            else:
                i-=1
                
        return False

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        output = False
        for lst in matrix:
            if lst[0] <= target and target <= lst[-1]:
                if target in lst:
                    output = True
                    break
        
        return output


class Solution:
    def checkRow(self, arr: List[int], target: int) -> bool:
        for i in arr:
            if i < target:
                continue
            elif i > target:
                return False
            else:
                return True

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            if self.checkRow(arr, target):
                return True
            continue
        return False
"""
