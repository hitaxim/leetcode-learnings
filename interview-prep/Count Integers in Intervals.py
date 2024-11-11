import bisect
from operator import itemgetter

class CountIntervals:

    def __init__(self):
	# initialize the merged intervals list as below to handle edge cases
        self.interv = [(float("-inf"), float("-inf")), (float("inf"), float("inf"))]
        self.cov = 0   

    def add(self, left: int, right: int) -> None:
        
        interv = self.interv
        
		# find the left most position for inserting of the new potentially merged interval
		# we use `left - 1` because the interval coverage is inclusive
        li = bisect.bisect_left(interv, left - 1, key=itemgetter(1))
        lval = min(interv[li][0], left)
		
		# find the right most position for inserting the new potentially merged interval
		# we use `right + 1` because the interval coverage is inclusive
        ri = bisect.bisect_right(interv, right + 1, key=itemgetter(0))
        rval = max(interv[ri - 1][1], right)

		# find the coverage of the intervals that will be replaced by the new interval
        to_delete = 0
        for _ in range(li, ri):
            to_delete += interv[_][1] - interv[_][0] + 1
            
		# udpate the coverage
        self.cov += rval - lval + 1 - to_delete
        interv[li: ri] = [(lval, rval)]

    def count(self) -> int:
        return self.cov

"""
from sortedcontainers import SortedList
class CountIntervals:

    def __init__(self):
        self.sorted_list = SortedList()
        self.num = 0
        
    def add(self, left: int, right: int) -> None:
        self.sorted_list.add([left,0])
        self.sorted_list.add([right,1])

        self.num += right - left + 1

        idx1 = self.sorted_list.index([left, 0])
        idx2 = self.sorted_list.index([right, 1])

        if idx1 - 1 >= 0 and self.sorted_list[idx1 - 1][1] == 0: 
            idx1 -= 1
        if idx2 + 1 < len(self.sorted_list) and self.sorted_list[idx2 + 1][1] == 1: 
            idx2 += 1
        
        if idx2 - idx1 != 1: 
            j = idx1 + 1
            for _ in range(idx1 + 1, idx2):
                if self.sorted_list[j][1] == 0:  # start 
                    self.num -= (self.sorted_list[j+1][0] - self.sorted_list[j][0] + 1)
                self.sorted_list.pop(j)
        
    def count(self) -> int:
        return self.num
"""
        
# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
