class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxR = -1

        for i in range(n-1, -1, -1):
            curr = arr[i]
            arr[i] = maxR
            maxR = max(maxR, curr)
        
        return arr
        
