class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        cnt = Counter(dict(nums1))
        cnt.update(dict(nums2))
        return sorted(cnt.items())
        
