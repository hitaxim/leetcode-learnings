class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        s1_words = deque(sentence1.split())
        s2_words = deque(sentence2.split())

        while s1_words and s2_words and s1_words[0] == s2_words[0]:
            s1_words.popleft()
            s2_words.popleft()
        
        while s2_words and s1_words and s1_words[-1] == s2_words[-1]:
            s1_words.pop()
            s2_words.pop()

        return not s2_words or not s1_words
