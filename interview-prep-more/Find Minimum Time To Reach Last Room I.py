"""
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        min_time = [[float("inf") for _ in range(n)] for _ in range(m)]
        min_time[0][0] = 0
        pq = [(0, 0, 0)]
        while pq:
            cur_time, i, j = heapq.heappop(pq)
            if i == m - 1 and j == n - 1: return cur_time
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if ni < 0 or ni == m or nj < 0 or nj == n: continue
                new_time = max(cur_time, moveTime[ni][nj]) + 1
                if min_time[ni][nj] > new_time:
                    min_time[ni][nj] = new_time
                    heapq.heappush(pq, (new_time, ni, nj))
        return 0
"""

import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        numRows = len(moveTime)
        numCols = len(moveTime[0])
        
        # Priority queue to store (current_time, x, y)
        minHeap = [(0, 0, 0)]  # Start at (0, 0) with time 0
        arrivalTime = [[float('inf')] * numCols for _ in range(numRows)]
        arrivalTime[0][0] = 0
        
        # Directions for adjacent rooms (down, up, right, left)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while minHeap:
            currentTime, x, y = heapq.heappop(minHeap)

            # If we reached the target room (numRows - 1, numCols - 1)
            if (x, y) == (numRows - 1, numCols - 1):
                return currentTime

            # Explore adjacent rooms
            for dx, dy in directions:
                newX, newY = x + dx, y + dy

                if 0 <= newX < numRows and 0 <= newY < numCols:
                    waitTime = max(moveTime[newX][newY] - currentTime, 0)
                    newArrivalTime = currentTime + 1 + waitTime

                    # Only push to the queue if we found a better arrival time
                    if newArrivalTime < arrivalTime[newX][newY]:
                        arrivalTime[newX][newY] = newArrivalTime
                        heapq.heappush(minHeap, (newArrivalTime, newX, newY))

        return -1  # Return -1 if the target room is unreachable
