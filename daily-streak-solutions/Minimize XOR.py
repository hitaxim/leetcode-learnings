class Solution:
    def minimizeXor(self, num1: int, num2: int, mxbits = 31) -> int:

        num1 = bin(num1)[2:].rjust(mxbits,'0') 
        bitNum =bin(num2).count('1')
        ans = ['0'] * mxbits

        for i in range(mxbits):
            if num1[i] == '1':
                ans[i] = '1'
                bitNum-= 1
                if bitNum == 0: break
                
        else:
            for i in range(mxbits - 1, -1, -1):
 
                if num1[i] == '0':
                    ans[i] = '1'
                    bitNum-= 1
                    if bitNum == 0: break

        return int(''.join(ans),2)

"""
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        sb = bin(num2).count("1")
        sa = bin(num1).count("1")
        if sa >= sb:
            for i in range(sa-sb):
                num1 &= num1 - 1
            return num1
        else:
            for i in range(sb-sa):
                num1 |= num1 + 1
            return num1
"""
