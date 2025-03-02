class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Extract all letters and reverse them
        letters = [char for char in s if char.isalpha()]
        letters.reverse()
        
        # Iterator for the reversed letters
        letter_iter = iter(letters)
        
        # Rebuild the string with letters replaced
        result = ''.join(next(letter_iter) if char.isalpha() else char for char in s)
        
        return result  

"""
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alphabets = [i for i in s if i.isalpha()][-1::-1]
        for i in range(len(s)):
            if not(s[i].isalpha()):
                alphabets.insert(i,s[i])
        alphabets = ''.join(alphabets)
        return alphabets
        
"""
