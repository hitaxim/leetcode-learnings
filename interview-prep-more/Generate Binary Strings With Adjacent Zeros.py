class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans=["0","1"]
        while (n>0):
            if n==1:
                return ans
            else:
                for i in range(len(ans)): #edit each string in answer list
                    if ans[i][len(ans[i])-1]=="0":       #if string ends with 0 add 1 in end
                        ans[i]=ans[i]+"1"
                    else: #if string ends with 1 add 1 more string same string with 1 in end and change the orginal string to end it with 0
                        ans.append(ans[i]+"1")
                        ans[i]=ans[i]+"0"
            n-=1

                        

"""
class Solution:
    def __init__(self):
        self.ans = []

    def f(self, prev: int, str_: str, n: int):
        if len(str_) == n:
            self.ans.append(str_)
            return
        self.f(1, str_ + '1', n)
        if prev == 1:
            self.f(0, str_ + '0', n)

    def validStrings(self, n: int) -> List[str]:
        self.ans = []
        self.f(0, "0", n)
        self.f(1, "1", n)
        return self.ans
"""    
            
