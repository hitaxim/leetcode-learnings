class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result = []
        test = []
        for n in nums:
            if n in test:
                result.append(n)
            else:
                test.append(n)
        return result
