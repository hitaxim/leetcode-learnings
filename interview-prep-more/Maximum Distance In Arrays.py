class Solution(object):
    def maxDistance(self, arrays):
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            max_distance = max(max_distance, abs(arr[-1] - smallest), abs(biggest - arr[0]))
            smallest = min(smallest, arr[0])
            biggest = max(biggest, arr[-1])

        return max_distance

"""
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minVal = float("inf")
        maxVal = float("-inf")
        res = 0
        for a in arrays:
            res = max(res, a[-1] - minVal, maxVal - a[0])
            minVal = min(a[0], minVal)
            maxVal = max(a[-1], maxVal)
        return res
"""
