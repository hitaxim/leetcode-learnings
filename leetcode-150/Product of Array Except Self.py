class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_num = len(nums)
        prefix_s = [1] * len_num
        suffix_s = [1] * len_num
       
        for i in range(1, len_num):
            prefix_s[i] = prefix_s[i-1] * nums[i-1]
        
        for j in range(len_num-2, -1, -1):
            suffix_s[j] = suffix_s[j+1] * nums[j+1]
        ans = [suffix_s[i] * prefix_s[i] for i in range(len_num)]
        return ans
