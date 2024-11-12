class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cache = defaultdict(int)
        pairs = 0

        for n in nums:
            cache[n] += 1

            if cache[n] % 2 == 0: 
                pairs += 1
        
        return [pairs, len(nums) - pairs * 2]

"""
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d=dict()
        l=[0,0]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
                if d[i]==2:
                    l[0]+=1
                    d[i]=0
        for i in d:
            if d[i]!=0:
                l[1]+=1
        return l
"""
