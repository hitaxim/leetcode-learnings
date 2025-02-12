class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        # Flatten the matrix into a 1D list
        ans = [num for row in matrix for num in row]

        # Sort the list to get k-th smallest element
        ans.sort()
        
        return ans[k-1]
