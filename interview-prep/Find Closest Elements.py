class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        
        # Binary search to find the closest window of k elements
        while left < right:
            mid = (left + right) // 2
            # Compare the difference between x and arr[mid] and arr[mid + k]
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        # The window of closest k elements starts from index `left`
        return arr[left:left + k]
