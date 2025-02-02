class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        result =[]
        def dfs(path):
            if len(path) == len(nums):
                result.append(path[:])
                return 
            for x in counter:
                if counter[x] > 0:
                    counter[x] -=1
                    path.append(x)
                    dfs(path)
                    path.pop()
                    counter[x] +=1
        dfs([])
        return result   
