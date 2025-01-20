class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr=[]
        res=[]
        for i in range(m):
            arr.append(i+1)

        for i in range(len(queries)):
            ind=arr.index(queries[i])
            arr.pop(ind)
            res.append(ind)
            arr.insert(0,queries[i])
        return res
