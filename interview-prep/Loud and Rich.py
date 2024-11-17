class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n=len(quiet)
        indegree=[0]*n
        lst=[[] for i in range(n)]
        for i,j in richer:
            lst[i].append(j)
            indegree[j]+=1
        ans=[i for i in range(n)]
        value=[quiet[i] for i in range(n)]
        st=[]
        for i in range(n):
            if indegree[i]==0:
                st.append(i)
        while st:
            x=st.pop(0)
            for i in lst[x]:
                indegree[i]-=1
                if value[x]<value[i]:
                    ans[i]=ans[x]
                    value[i]=value[x]
                if indegree[i]==0:
                    st.append(i)
        return ans
                

        
