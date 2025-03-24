class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        meetings.sort(key=lambda x: x[0])
        count = abs(meetings[0][0] - 1)
        n = len(meetings)
        for i in range(1, n):
            if meetings[i][0] <= meetings[i - 1][1]:
                if meetings[i][1] < meetings[i - 1][1]:
                    meetings[i][1] = meetings[i - 1][1]
            else:
                dy = meetings[i][0] - meetings[i - 1][1]
                count += dy - 1
        count += abs(meetings[n - 1][1] - days)
        return count
