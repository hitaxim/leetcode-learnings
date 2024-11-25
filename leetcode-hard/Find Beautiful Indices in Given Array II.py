class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        if len(set(a))==len(set(b))==len(set(s))==1:
            return [i for i in range(max(0,len(s)-(len(a)-1)))]
        
        i = s.find(a)
        j = s.find(b)
        sol= []
        n = len(a)
        m = len(b)
        while i!=-1 and j!=-1:
            if abs(i-j)<=k:
                sol.append(i)
                i=s.find(a,i+1)
                continue
            if i<j:
                i = s.find(a,i+ 1)
            else:
                j = s.find(b,j+1)
        return sol
