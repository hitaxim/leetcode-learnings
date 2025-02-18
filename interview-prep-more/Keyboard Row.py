
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Define keyboard rows
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []  # To store valid words
        
        for word in words:
            # Convert word to lowercase for case-insensitivity
            lowercase_word = set(word.lower())
            
            # Check if the word can be typed using one row
            if lowercase_word <= row1 or lowercase_word <= row2 or lowercase_word <= row3:
                result.append(word)
        
        return result
