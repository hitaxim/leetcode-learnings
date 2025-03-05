def spiral_order(matrix):
        # Initialize boundaries
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        ans = []
        
        # Continue while there are boundaries to process
        while left <= right and top <= bottom:
            # Traverse from left to right along the top boundary
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1  # Shrink the top boundary
            
            # Traverse from top to bottom along the right boundary
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1  # Shrink the right boundary
            
            # Check if boundaries have crossed
            if not (left <= right and top <= bottom):
                break
            
            # Traverse from right to left along the bottom boundary
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1  # Shrink the bottom boundary
            
            # Traverse from bottom to top along the left boundary
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1  # Shrink the left boundary
        
        return ans
        
