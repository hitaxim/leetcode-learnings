class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        l=defaultdict(int)
        l[0]+=1
        for num in nums:
            newl=defaultdict(int)
            for i in l:
                newl[i+num]+=l[i]
                newl[i-num]+=l[i]
            l=newl
        return l[target]
