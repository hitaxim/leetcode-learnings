class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i,len(nums)):
                curr = lcm(curr,nums[j])
                if curr == k: count+=1
                if curr > k:
                    break
        return count

"""
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def find_lcm(a, b):
            return abs(a * b) // gcd(a, b)
        c=0
        for i in range(len(nums)):
            l=nums[i]
            if l==k:
                c+=1
            if l>k:
                continue
            for j in range(i+1,len(nums)):
                l=find_lcm(l,nums[j])
                if l==k:
                    c+=1
                if l>k:
                    break
        return c

"""



        
