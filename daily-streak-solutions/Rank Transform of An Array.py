class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_s = sorted(set(arr))
        rank_d = {}
        for i, val in enumerate(sorted_s):
            rank_d[val] = i+1
        return [rank_d[num] for num in arr]
