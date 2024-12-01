class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        rem = defaultdict(int)
        ans = 0 

        for i in hours:
            k = (24 - i % 24) % 24
            if k in rem: 
                ans += rem[k]
            rem[i % 24] += 1

        return ans
        
