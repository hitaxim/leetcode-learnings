class RecentCounter:

   def __init__(self):
       self.record = []
       self.start = 0

   def ping(self, t: int) -> int:
       self.record.append(t)
       while self.record[self.start] < t - 3000:
           self.start += 1
       return len(self.record) - self.start
