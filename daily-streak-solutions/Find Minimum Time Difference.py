class Solution:
   def findMinDifference(self, timePoints: List[str]) -> int:
       mins_arr = []
       for timepoint in timePoints:
           h, m = map(int,timepoint.split(':'))
           mins = h * 60 + m
           mins_arr.append(mins)
      
       mins_arr.sort()
       res = float('inf')
       for i in range(1, len(mins_arr)):
           res = min(res, mins_arr[i] - mins_arr[i-1])
      
       return min(res, 1440 + mins_arr[0] - mins_arr[-1])
