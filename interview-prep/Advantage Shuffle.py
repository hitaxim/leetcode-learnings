class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ## Sort num1 -> ascending and num2 -> descending
        
        q = deque(sorted(nums1))
        n = len(nums1)

        order = sorted(range(n), key = lambda x: nums2[x], reverse = True)
        res = [0] * n

        for idx in order:
            if q[-1] > nums2[idx]:
                res[idx] = q.pop()
            else:
                res[idx] = q.popleft()
        
        return res  
