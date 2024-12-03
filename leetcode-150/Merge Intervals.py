class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        k = 0

        for i in range(1, len(intervals)):
            if intervals[k][1] >= intervals[i][0]:
                intervals[k][1] = max(intervals[k][1], intervals[i][1])
            else: 
                k += 1
                intervals[k] = intervals[i]
        
        return intervals[:k+1]
