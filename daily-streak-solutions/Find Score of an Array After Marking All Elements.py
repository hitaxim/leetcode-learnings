class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted((num, idx) for idx, num in enumerate(nums))
        score = 0

        for num, idx in sorted_nums:
            if nums[idx] != -1:  # Process only if not already marked
                score += num
                nums[idx] = -1  # Mark current index
                if idx > 0:
                    nums[idx - 1] = -1  # Mark left neighbor
                if idx < n - 1:
                    nums[idx + 1] = -1  # Mark right neighbor

        return score
  
"""
  class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        # Build a min-heap with (value, index) pairs
        min_heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(min_heap)  # Convert to a min-heap

        score = 0  # Initialize score

        # Process elements in min-heap
        while min_heap:
            num, idx = heapq.heappop(min_heap)  # Get the smallest unprocessed element
            if nums[idx] != -1:  # Process only if not already marked
                score += num
                nums[idx] = -1  # Mark the current index
                if idx > 0 and nums[idx - 1] != -1:
                    nums[idx - 1] = -1  # Mark the left neighbor
                if idx < n - 1 and nums[idx + 1] != -1:
                    nums[idx + 1] = -1  # Mark the right neighbor

        return score

class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        n = len(nums)
        q = deque()

        # Traverse through the array
        for i in range(n):
            # If queue is not empty and the current number is greater than or equal to the last in queue
            if q and nums[i] >= q[-1]:
                skip = False
                # Process the elements in the queue
                while q:
                    add = q.pop()
                    if not skip:
                        score += add
                    skip = not skip
                continue

            # Add current element to the queue
            q.append(nums[i])

        # Final processing of remaining elements in the queue
        skip = False
        while q:
            add = q.pop()
            if not skip:
                score += add
            skip = not skip

        return score
    
"""
