class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        max_len = 0

        for i in range(len(nums)):
            if visited[i]:
                continue
            
            length = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = nums[j]
                length += 1
            
            max_len = max(length, max_len)
        
        return max_len
   
