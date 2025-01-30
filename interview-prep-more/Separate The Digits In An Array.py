class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st = []
        for i in range(len(nums)):
            for j in str(nums[i]):
                st.append(int(j))
        return st
