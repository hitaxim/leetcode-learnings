class MyCalendar:

    def __init__(self):
        self.bookings = [ (-1,-1), (float('inf'), float('inf')) ]

    def book(self, start: int, end: int) -> bool:
        # Use bisect to efficiently find the insertion point for the new booking's end date
        index = bisect_left(self.bookings, (start, end))

        # Check for clash with previous booking (if any)
        if start < self.bookings[index - 1][1]:
            return False

        # Check for clash with next booking (if any)
        if end > self.bookings[index][0]:
            return False

        # No clash found, insert the new booking at the appropriate position
        self.bookings.insert(index, (start, end))
        return True

ORRRRRR

class MyCalendar:

    def __init__(self):
        self.booked = []
        
    def book(self, start: int, end: int) -> bool:
        if self.check_booking(start, end):
            self.booked.append([start, end])
            return True
        return False
    
    def check_booking(self, start: int, end: int):
        for s, e in self.booked: 
            # Check 2 conditions for start and end : e(x+1,y), s(x,y-1)
            if (start >= s and start <= e-1) or (end >= s+1 and end <= e ):
                return False
            if s > start and e < end: 
                return False
        return True
