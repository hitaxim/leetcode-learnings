class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")

        for id, w in enumerate(words): 
            if w.startswith(searchWord): 
                return id + 1
                
        return -1
