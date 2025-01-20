class Solution:
    def isThree(self, n: int) -> bool:
        return sum(n%i == 0 for i in range(1, n+1)) == 3

"""
class Solution:
    def isThree(self, n: int) -> bool:
        root = int(n ** 0.5)
        if root * root != n:
            return False
        
        for i in range(2, root):
            if root % i == 0:
                return False
        return root > 1

class Solution:
    def isThree(self, n: int) -> bool:
        import math
        cnt=2
        for i in range(2,math.floor(math.sqrt(n))+1)  :
            if n%i==0:
                cnt+=1
                if n//i!=i:
                    cnt+=1
            if cnt>3:
                return False
        if cnt<3:
            return False
        return True
    
"""
