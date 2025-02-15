class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        
        @lru_cache(None)
        def dp(i: int, op1: int, op2: int)-> int:

            if i == len(nums): return 0
            num = nums[i]
            i+= 1
            res = [num + dp(i, op1, op2)]
            
            if op1 and op2:
                if half(num) >= k:              
                    res.append(subt(half(num)) + dp(i, op1 - 1, op2 - 1))
                elif num >= k:
                    res.append(half(subt(num)) + dp(i, op1 - 1, op2 - 1))
            
            if op1:
                res.append(half(num) + dp(i, op1 - 1, op2))
                
            if op2 and num >= k:
                res.append(subt(num) + dp(i, op1, op2 - 1))

            return min(res)
        

        subt = lambda x: max(x - k, 0)
        half = lambda x: (x + 1)//2

        return dp(0, op1, op2)
