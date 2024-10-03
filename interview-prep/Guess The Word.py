class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        while words:
            searchW = random.choice(words)
            deleteIndex = set()
            score = [0] * len(words)
            currScore = master.guess(searchW)
            if currScore == 6: 
                return 
            else:
                for a in range(len(words)):
                    for b in range(6):
                        if words[a][b] == searchW[b]:
                            score[a] += 1
                for r in range(len(score)):
                    if score[r] != currScore:
                        deleteIndex.add(r)
                for index in sorted(deleteIndex, reverse= True):
                    words.pop(index)
                    score.pop(index)
                deleteIndex.clear()

ORRRRRR

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def similarity(word1, word2):
            counter = 0
            for w1, w2 in zip(word1, word2):
                if w1 == w2:
                    counter += 1
            return counter

        guess_word = random.choice(words)
        score = master.guess(guess_word)
        while score < 6:
            words = list(filter(lambda word: similarity(word, guess_word) == score, words))
            guess_word = random.choice(words)
            score = master.guess(guess_word)
