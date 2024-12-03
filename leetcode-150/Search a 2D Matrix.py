class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r : 
            mid = l + (r - l) // 2
            midVal = matrix[mid // n][mid % n]

            if midVal == target:
                return True
            elif midVal < target:
                l = mid + 1
            else: 
                r = mid - 1
        
        return False
