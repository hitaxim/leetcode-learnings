class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n_d = len(digits)
        dict_ans = {"2":"abc", "3":"def", "4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if not digits: 
            return []
        iterable_list = [dict_ans[val] for val in digits]
        return ["".join(x) for x in itertools.product(*iterable_list)]

ORRRRRRR

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n_d = len(digits)
        dict_ans = {"2":"abc", "3":"def", "4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if not digits: 
            return []

        def backtrack(idx, comb):
            if idx == n_d:
                ans.append(comb[:])
                return 

            for l in dict_ans[digits[idx]]:
                backtrack(idx+1, comb+l)
        
        ans = []
        backtrack(0,"")

        return ans
