class Solution:
    def checkValidCuts(self, n, rectangles):
        rx = []
        ry = []
        for sx, sy, ex, ey in rectangles:
            rx.append((sx, ex))
            ry.append((sy, ey))

        def can_insert(intervals):
            intervals.sort()
            interval_ends = []
            heapq.heappush(interval_ends, intervals[0][1])
            n = len(intervals)
            partitions = 0
            for i in range(1, n):
                interval = intervals[i]
                while interval_ends and interval[0] >= interval_ends[0]:
                    heapq.heappop(interval_ends)
                if not interval_ends:
                    partitions += 1
                heapq.heappush(interval_ends, intervals[i][1])
            return partitions >= 2

        return can_insert(rx) or can_insert(ry)
