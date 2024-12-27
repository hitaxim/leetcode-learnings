class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = temp = 0
        for i, value in enumerate(values):           
            ans = max(ans, temp + value - i)
            temp = max(temp, value + i)
        return ans

"""
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxVal = 0
        curr = 0
        for i in range(1, len(values)):
            curr = max(curr, values[i-1]+i-1)
            maxVal = max(maxVal, curr + values[i]-i)
        return maxVal
"""     
