class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n = max(nums1[-1][0], nums2[-1][0])
        merge = [0] * n 

        for idx, val in nums1:
            merge[idx] += val 
        for idx, val in nums2:
            merge[idx] += val 
        
        res = []
        for idx, val in enumerate(merge):
            if val > 0:
                res.append([idx, val])
                
        return res
        
