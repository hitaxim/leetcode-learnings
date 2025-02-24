class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        lg = max(nums)
        ig = nums.index(lg)
        del nums[ig]
        sg = max(nums)

        if sg > lg/2:
            return -1
        else:
            return ig
