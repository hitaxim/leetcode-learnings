class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq=[0]*101
        maxF=0
        for x in nums:
            freq[x]+=1
            maxF=max(maxF, freq[x])
        ans=0
        for f in freq:
            if f==maxF:
                ans+=f
        return ans


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        counter = list(counter.values())
        maxCount = max(counter)
        return counter.count(maxCount) * maxCount
