class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r ,output, n =0, 0, 0, len(arr)
        if n==1:
            return 1
        while r < n:
            while r<n-1 and (arr[r-1]>arr[r]<arr[r+1] or arr[r-1]<arr[r]>arr[r+1]):
                r+=1
            while l < r and arr[l]==arr[l+1]:
                l+=1
            output = max(output,r-l+1)
            
            l=r
            r+=1
        return output
        
