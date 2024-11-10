class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_len = float('inf')
        or_to_index = {}

        for right, num in enumerate(nums):
            new_or_values = {or_val | num: left for or_val, left in or_to_index.items()}
            new_or_values[num] = right
            or_to_index = new_or_values

            for or_val, left in or_to_index.items(): 
                if or_val >= k: 
                    min_len = min(min_len, right - left + 1)
        
        return min_len if min_len != float('inf') else -1
