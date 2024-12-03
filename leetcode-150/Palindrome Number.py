class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = str(x)
        if l == l[::-1]: 
            return True
        else: 
            return False
