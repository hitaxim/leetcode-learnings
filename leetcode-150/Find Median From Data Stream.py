class MedianFinder:

    def __init__(self):
        self.minq = []
        self.maxq = []

    def addNum(self, num: int) -> None:
        heappush(self.minq, -heappushpop(self.maxq, -num))
        if len(self.minq) - len(self.maxq) > 1:
            heappush(self.maxq, -heappop(self.minq))

    def findMedian(self) -> float:
        if len(self.minq) == len(self.maxq):
            return (self.minq[0] - self.maxq[0]) / 2
        return self.minq[0]

"""
import statistics

class MedianFinder:

    def __init__(self):
        self.ans = []

    def addNum(self, num: int) -> None:
        for i in range(len(self.ans)):
            if(num<= self.ans[i]):
                self.ans.insert(i, num)
                return 
        self.ans.append(num)

    def findMedian(self) -> float:
        return statistics.median(self.ans)
        
"""
