class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Create a list to store the pair (end time, value) for events
        pq = []

        # Sort the events by their start time
        events.sort(key=lambda x: x[0])

        maxVal = 0
        maxSum = 0

        for event in events:
            # Pop all valid events from the priority queue and take their maximum
            while pq and pq[0][0] < event[0]:
                maxVal = max(maxVal, pq[0][1])
                heapq.heappop(pq)

            # Calculate the maximum sum by adding the current event's value and the best previous event's value
            maxSum = max(maxSum, maxVal + event[2])

            # Push the current event's end time and value into the heap
            heapq.heappush(pq, (event[1], event[2]))

        return maxSum
        

"""
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Step 1: Sort the events based on their end time
        events.sort(key=lambda x: x[1])
        
        # Step 2: Maintain a list of [endTime, max_value_until_now]
        max_until = []
        max_value = 0
        for _, end, value in events:
            max_value = max(max_value, value)
            max_until.append((end, max_value))
        
        # Step 3: Find the maximum sum of two events
        result = 0
        for start, end, value in events:
            # Option 1: Take the current event alone
            result = max(result, value)
            
            # Option 2: Take another event that ends before this one starts
            idx = bisect.bisect_left(max_until, (start, 0)) - 1
            if idx >= 0:
                result = max(result, value + max_until[idx][1])
        
        return result
"""
