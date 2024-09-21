class Solution:
   def lexicalOrder(self, n: int) -> List[int]:
       heap = []
       ans = []
       for i in range(1, n+1):
           heapq.heappush(heap, str(i))
       while heap:
           ans.append(int(heapq.heappop(heap)))
       return ans
