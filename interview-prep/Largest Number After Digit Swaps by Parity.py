class Solution:
    def largestInteger(self, num: int) -> int:
        digits = [int(digit) for digit in str(num)]

        even = []
        odd = []
        for digit in digits:
            if digit % 2 == 0:
                even.append(digit)
            else:
                odd.append(digit)
        
        even.sort(reverse = True)
        odd.sort(reverse = True)

        ans = []
        for digit in digits:
            if digit % 2 == 0:
                ans.append(even.pop(0))
            else:
                ans.append(odd.pop(0))
        
        ans = int("".join(map(str, ans)))

        return ans
        
