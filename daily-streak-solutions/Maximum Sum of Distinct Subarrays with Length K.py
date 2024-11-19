class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maps = defaultdict(int)
        win_s = 0
        max_sum = 0

        for i in range(n):
            # Add element to window
            maps[nums[i]] += 1
            win_s += nums[i]

            # If window size increases 'k', slide window
            if i >= k:
                le = nums[i - k]
                maps[le] -= 1
                win_s -= le
                if maps[le] == 0: 
                    del maps[le]
            
            if i >= k - 1 and len(maps) == k:
                max_sum = max(max_sum, win_s)

        return max_sum
