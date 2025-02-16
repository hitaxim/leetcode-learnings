class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.s = sum(nums)
        self.n = len(nums)

    def update(self, index: int, val: int) -> None:
        self.s = self.s-self.nums[index]+val
        self.nums[index] = val
        
        

    def sumRange(self, left: int, right: int) -> int:
        #for some reason finding from both ends and removing it works.
        #left
        sL = sR = 0
        for i in range(left):
            sL+=self.nums[i]
        for j in range(right+1,self.n):
            sR+=self.nums[j]
        return self.s-sL-sR
