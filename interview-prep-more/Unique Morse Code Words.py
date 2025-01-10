class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [
                ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
                ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
                "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
            ]
        
        unique_transformations = set()
        for word in words:
                transformation = ''.join(morse_code[ord(char) - ord('a')] for char in word)
                unique_transformations.add(transformation)

            
        return len(unique_transformations)
