class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        lm = 0  # Last index at which "M" was seen
        lg = 0  # Last index at which "G" was seen
        lp = 0  # Last index at which "P" was seen
        ans = 0

        for i in range(len(garbage)):
            if "G" in garbage[i]:
                lg = i
            if "P" in garbage[i]:
                lp = i
            if "M" in garbage[i]:
                lm = i
            ans+=len(garbage[i])

        ans+=sum(travel[:lm])+sum(travel[:lg])+sum(travel[:lp])

        return ans   
