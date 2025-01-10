class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        st, res = set(), "" #res == result
        st.add("")
        for word in words:
            if word[:-1] in st:
                if len(word) > len(res):
                    res = word
                st.add(word)
        
        return res
        
