class Solution:
    def wiggleMaxLength(self, nums):
        if not nums:
            return 0

        count = 1
        dif = None  # Use None to represent undefined

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if dif == 1 or dif is None:
                    dif = 0
                    count += 1
            elif nums[i] < nums[i + 1]:
                if dif == 0 or dif is None:
                    dif = 1
                    count += 1

        return count
