class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        t=0
        for i in range(len(timeSeries)):
            if i==0:
                t+=duration
            else:
                diff=timeSeries[i]-timeSeries[i-1]
                if diff>=duration:
                    t+=duration
                else:
                    t+=diff
        return t

"""
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = duration

        for i in range(1, len(timeSeries)):
            # no overlap
            if timeSeries[i] > timeSeries[i-1] + duration - 1:
                res += duration

            # yes overlap
            else:
                res += timeSeries[i] - timeSeries[i-1]

        return res
"""
