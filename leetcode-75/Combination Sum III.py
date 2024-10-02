class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        if k > n: 
            return ans

        def backtrack(index, prev, total):
            if len(prev) == k: 
                if total == n:
                    ans.append(prev)
                return 

            for i in range(index,10):
                curr = total + i
                if curr <= n: 
                    backtrack(i+1,prev+[i],curr)
                
        backtrack(1,[],0)
        return ans
