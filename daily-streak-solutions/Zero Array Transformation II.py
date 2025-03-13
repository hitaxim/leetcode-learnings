class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        
    
        q = queries[::-1]
        
        delta = [0] * (n + 1)
        current_sum = 0
        
        for i, num in enumerate(nums):
           
            current_sum += delta[i]
            
         
            while q and current_sum < num:
                start, end, val = q.pop()
                
                if end >= i:
                    if start <= i:
                      
                        current_sum += val
                    else:
                    
                        delta[start] += val
                    
              
                    delta[end + 1] -= val
            
         
            if current_sum < num:
                return -1
        
        return m - len(q)
