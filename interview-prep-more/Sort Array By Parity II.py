class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        new = []
        mew = []
        no = []
        for i in range(len(nums)):
            if nums[i]%2==0:
                new.append(nums[i])
            else:
                mew.append(nums[i])
        for i in range(len(new)):
            no.append(new[i])
            no.append(mew[i])
        return no
        

        
