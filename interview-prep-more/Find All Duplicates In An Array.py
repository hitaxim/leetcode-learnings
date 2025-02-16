class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mp = {}
        for i in nums:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] += 1
        
        res = []
        for i, v in mp.items():
            if v == 2:
                res.append(i)
        return res

"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count_num = Counter(nums)
        result = []
        for keys, values in count_num.items():
            if values == 2:
                result.append(keys)

        return result
        
"""
