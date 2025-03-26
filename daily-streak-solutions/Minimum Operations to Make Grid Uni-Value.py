class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid into a single list.
        temp = [num for row in grid for num in row]
        temp.sort()
        
        # Check if it's possible to equalize all elements.
        rem = temp[0] % x
        for num in temp:
            if num % x != rem:
                return -1
        
        # Select the median as the target.
        n = len(temp)
        median = temp[n // 2]
        
        # Compute the total number of operations.
        operations = sum(abs(num - median) // x for num in temp)
        return operations
