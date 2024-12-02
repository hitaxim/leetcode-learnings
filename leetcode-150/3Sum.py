class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue

            l,r = i + 1, len(nums) - 1
            while l < r:
                threesum = num + nums[l] + nums[r]

                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        neg = defaultdict(int)
        pos = defaultdict(int)
        zeros = 0 
        for n in nums: 
            if n < 0: 
                neg[n] += 1
            elif n > 0: 
                pos[n] += 1
            else: 
                zeros += 1
        
        result = []
        if zeros: 
            for n in neg: 
                if -n in pos: 
                    result.append((0, n, -n))
            if zeros > 2: 
                result.append((0,0,0))
        
        for set1, set2 in ((neg, pos), (pos, neg)):
            set1Items = list(set1.items())
            for i, (j, k) in enumerate(set1Items):
                for j2, k2 in set1Items[i:]:
                    if j != j2 or (j==j2 and k >1):
                        if -j-j2 in set2: 
                            result.append((j, j2, -j-j2))
        return result
"""
