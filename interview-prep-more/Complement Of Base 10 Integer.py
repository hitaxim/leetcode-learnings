class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a=bin(n)
        a=list(a[2:])
        print(a)
        for i in range(len(a)):
            if(a[i]=='0'):
                a[i]='1'
            else:
                a[i]='0'
        return int(str("".join(a)),2)


        
