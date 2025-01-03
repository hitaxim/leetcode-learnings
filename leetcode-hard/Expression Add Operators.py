class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = set()

        def backtrack(i, total, last, expr):
            if i == n:
                if total == target:
                    ans.add(expr)
                return 
            
            for j in range(i, n):
                nums = int(num[i:j+1])
                if i == 0:
                    backtrack(j +1, nums, nums, str(nums))
                else:
                    backtrack(j +1, total + nums, nums, expr + "+" + str(nums))
                    backtrack(j + 1, total - nums, -nums, expr + "-" + str(nums))
                    backtrack(j +1, total - last + last * nums, last * nums, expr + '*' + str(nums))
                if nums == 0:
                    break

        
        backtrack(0, 0, 0, '')
        return list(ans)
        
