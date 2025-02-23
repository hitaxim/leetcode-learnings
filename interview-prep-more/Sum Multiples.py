class Solution:
    def sumOfMultiples(self, n: int) -> int:
        res = 0
		#  iterate through the range 1 to n and 
        for i in range(3, n + 1):
			# count numbers divisible by either 3, 5, or 7
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                res += i
        return res

"""
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 3 * ((n//3)*(n//3 + 1))//2
        ans += 5 * ((n//5)*(n//5 + 1))//2
        ans += 7 * ((n//7)*(n//7 + 1))//2
        ans -= 15 * ((n//15)*(n//15 + 1))//2
        ans -= 21 * ((n//21)*(n//21 + 1))//2
        ans -= 35 * ((n//35)*(n//35 + 1))//2
        ans += 105 * ((n//105)*(n//105 + 1))//2
        return ans
"""
