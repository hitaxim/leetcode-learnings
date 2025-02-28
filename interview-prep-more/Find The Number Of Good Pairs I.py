class Solution:
    def numberOfPairs(self, nums1: List[int], 
                            nums2: List[int], k: int, ans = 0) -> int:

        nums1 = list(map(lambda x: x//k, filter(lambda x: x%k == 0, nums1)))
        
        for n1, n2 in product(nums1, nums2):
            
            if n1%n2 == 0: ans+= 1

        return ans
