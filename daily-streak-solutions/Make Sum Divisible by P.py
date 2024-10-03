class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        totalsum = sum(nums)
        rem = totalsum % p

        if rem == 0: 
            return 0

        hashmap1 = {0: -1}
        minlen = len(nums)
        prefix_sum = 0
        
        for i, x in enumerate(nums): 
            prefix_sum += x
            curr_mod =  prefix_sum % p
            targetmod = (curr_mod - rem + p) % p
        
            if targetmod in hashmap1:
                minlen = min(minlen, i - hashmap1[targetmod])
            hashmap1[curr_mod] = i
        
        return minlen if minlen < len(nums) else -1
