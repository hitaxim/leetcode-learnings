from sortedcontainers import SortedList
class MyCalendarTwo:

    def __init__(self):
        self.booked = SortedList()

    def book(self, start: int, end: int) -> bool:
        self.booked.add((start,1))
        self.booked.add((end, -1))
        total = 0
        for i, j in self.booked:
            total += j

            if total == 3:
                self.booked.remove((start,1))
                self.booked.remove((end, -1))
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
