class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prefixSum = [0]*n
        for i in range(1, n):
            if nums[i]%2 != nums[i - 1]%2:
                prefixSum[i] = 1 + prefixSum[i - 1]
            else:
                prefixSum[i] = prefixSum[i - 1]

        ans = []
        for left, right in queries:
            if prefixSum[right] - prefixSum[left] == right - left:
                ans.append(True)
            else:
                ans.append(False)

        return ans

"""
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        if len(nums) == 1:
            return [True] * len(queries)
        
        c = Counter()
        true_count = [0] * (len(nums))
        
        for i in range(len(nums)- 1):
            if nums[i] & 1 != nums[i+1] & 1:
                c += Counter([True])
            true_count[i+1] = c[True]
        
        ans = []
        for s, e in queries: 
            if true_count[e] - true_count[s] == e - s:
                ans.append(True)
            else: 
                ans.append(False)
        return ans
"""
