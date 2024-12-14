from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_window = SortedList()  # To maintain the current window's sorted elements
        start = 0
        total_subarrays = 0
        
        for end in range(n):
            # Add the current element to the sorted window
            sorted_window.add(nums[end])
            
            # Ensure the window is valid
            while sorted_window[-1] - sorted_window[0] > 2:
                # Remove the leftmost element from the window
                sorted_window.remove(nums[start])
                start += 1
            
            # Count valid subarrays ending at 'end'
            total_subarrays += end - start + 1
        
        return total_subarrays

"""
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        minqueue = deque()
        maxqueue = deque()

        result = 0
        left = 0

        for idx,val in enumerate(nums):
            while minqueue and minqueue[-1][1] >= val:
                minqueue.pop()
            minqueue.append((idx,val))

            while maxqueue and maxqueue[-1][1] <= val:
                maxqueue.pop()
            
            maxqueue.append((idx,val))

            while maxqueue[0][1] - minqueue[0][1] > 2:
                if maxqueue[0][0] == left:
                    maxqueue.popleft()
                
                if minqueue[0][0] == left:
                    minqueue.popleft()
                left += 1
            result += idx - left + 1
        return result
"""
