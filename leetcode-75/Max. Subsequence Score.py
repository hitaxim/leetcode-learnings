class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        heap = []
        totalSum = 0

        merged = [(nums2[i], nums1[i]) for i in range(len(nums1))]
        merged.sort(reverse=True)

        for x, val_num1 in merged: 
            if len(heap) == k: 
                totalSum -= heapq.heappop(heap)
            totalSum += val_num1
            heapq.heappush(heap, val_num1)

            if len(heap) == k: 
                ans = max(ans, totalSum * x)
        return ans
