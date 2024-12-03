class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []

        for i in range(min(k, len(nums2))):
            heappush(heap, (nums1[0] + nums2[i], 0, i))

        ans = []

        while heap and len(ans) < k:
            _, i, j = heappop(heap)
            ans.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1):
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))

        return ans
        
"""
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        pq = []

        for x in nums1:
            heapq.heappush(pq, [x + nums2[0], 0])

        while k > 0 and pq: 
            pair = heapq.heappop(pq)
            s, pos = pair[0], pair[1]

            res.append([s - nums2[pos], nums2[pos]])

            if pos + 1 < len(nums2):
                heapq.heappush(pq, [s - nums2[pos] + nums2[pos + 1], pos + 1])
        
            k -= 1

        return res
"""  
