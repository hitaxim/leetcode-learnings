class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        available_at = 0
        total_wait = 0

        for arrives, t in customers:
            available_at = max(available_at, arrives) + t
            total_wait += available_at - arrives

        return total_wait / len(customers)
     
