class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        for i in range(n):
            nums.append(start + 2 * i)
        num=nums[0]
        for i in range(1,len(nums)):
            num=num^nums[i]
        return num
