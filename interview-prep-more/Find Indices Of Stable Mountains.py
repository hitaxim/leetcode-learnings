class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:

        ans = []

        for i, (prv, mtn) in enumerate(pairwise(height)):
            if prv > threshold: ans.append(i+1)

        return ans   
