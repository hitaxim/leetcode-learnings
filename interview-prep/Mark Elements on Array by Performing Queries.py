class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        m = len(nums)
        mark = set()
        ans = []
        heap = [(value, i) for i, value in enumerate(nums)]
        heapq.heapify(heap)
        total_val = sum(nums)

        for index, k in queries:
            if index not in mark:
                mark.add(index)
                total_val -= nums[index]
            
            while k > 0 and heap:
                value, idx = heapq.heappop(heap)
                if idx not in mark:
                    mark.add(idx)
                    total_val -= value
                    k -= 1
            
            ans.append(total_val)

        return ans
        
