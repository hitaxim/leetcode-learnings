class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while (l < r and arr[l+1] >= arr[l]):
            l += 1
        if l == len(arr) - 1:  # array is sorted
            return 0 
        while r > 0 and arr[r-1] <= arr[r]:
            r -= 1

        rem = min(len(arr) - l - 1, r)
        for i in range(l+1):
            if arr[i] <= arr[r]:
                rem = min(rem, r-i-1)
            elif r < len(arr) - 1:
                r += 1
            else: 
                break
        return rem
