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
