class Solution:
    def equalFrequency(self, word: str) -> bool:
        freqs = sorted(list(Counter(word).values()))

        if len(freqs) == 1:
            return True

        if freqs[0] == 1:
            return freqs[1] == freqs[-1] or (freqs[-2] == 1 and freqs[-1] == 2)

        return freqs[0] == freqs[-2] and freqs[-1] - 1 == freqs[0]     
