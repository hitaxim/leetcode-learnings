class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        n1=n
        i=1
        while sum(map(int,str(n)))>target:
            n=(n//10)+1
            i*=10
            
        return ((n*i)-n1)   
