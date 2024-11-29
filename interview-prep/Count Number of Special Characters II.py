class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        wordSet = set(word)
        dic = {}
        
        ## SAVE UPPER ONES IN DICT WITH INDEX
        for i, ch in enumerate(word):
            if ch.isupper() and ch.lower() in wordSet:
                if ch not in dic:
                    dic[ch] = i

        # CHECK FOR LOWER LETTERS AND COMPARE INDEX
        for i, ch in enumerate(word):
            if ch.islower() and ch.upper() in dic:
                if i > dic[ch.upper()]:
                    dic.pop(ch.upper())
        
        return len(dic)
