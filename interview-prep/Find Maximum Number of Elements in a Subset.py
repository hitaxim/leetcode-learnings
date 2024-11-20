class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        hmap = Counter(nums)
        result = 1
        for n in hmap.keys():
            if hmap[n] > 1 and n != 1: 
                k = 2
                count = 2
                while n**k in hmap and hmap[n**k] >= 1: 
                    if hmap[n**k] == 1: 
                        count += 1
                        result = max(count, result)
                        break
                    else: 
                        count += 2
                        k *= 2
                else: 
                    result = max(result, count -1)
            elif n == 1: 
                if hmap[n] % 2 != 0: 
                    result = max(result, hmap[1])
                else: 
                    result = max(result, hmap[1]- 1)
        return result
        
