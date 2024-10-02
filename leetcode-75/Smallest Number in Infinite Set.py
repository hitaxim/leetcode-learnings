class SmallestInfiniteSet:

    def __init__(self):
        list1 = list(range(1,1001))
        self.obj = set(list1)

    def popSmallest(self) -> int:
        min_val = min(self.obj)
        self.obj.remove(min_val)
        return min_val

    def addBack(self, num: int) -> None:
        if num not in self.obj: 
            self.obj.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
import heapq
class SmallestInfiniteSet:

    def __init__(self):
        # heapq for addback
        self.heap = []
        # set for check duplicate
        self.set = set()
        # variable for track the current minmum num
        self.current = 1 # the minimum number current is 1

    def popSmallest(self) -> int:
        if self.heap:
            num = heapq.heappop(self.heap)
            self.set.remove(num)
            return num
        else:
            self.current += 1
            return self.current - 1


    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.set:
            heapq.heappush(self.heap, num)
            self.set.add(num)
        
