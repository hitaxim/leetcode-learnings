class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=str(x)
        Sum=0
        for i in range(len(s)):
            Sum+=int(s[i])
        if x%int(Sum)==0:
            return int(Sum)
        else:
            return -1
