class Solution:

    def countOfSubstrings(self, word: str, k: int) -> int:
        def countAtLeastMConsonants(m):
            n = len(word)
            vowels = ('a', 'e', 'i', 'o', 'u')
            vowels_map = defaultdict(int)
            num_consonants = 0
            ans = 0
            l = 0
            r = 0
            while r < n or l < n:
                if len(vowels_map) == 5 and num_consonants >= m:
                    ans += n - r + 1
                    if word[l] not in vowels:
                        num_consonants -= 1
                    else:
                        vowels_map[word[l]] -= 1
                        if vowels_map[word[l]] == 0:
                            del vowels_map[word[l]]
                    l += 1
                else:
                    if r == n:
                        break
                    if word[r] not in vowels:
                        num_consonants += 1
                    else:
                        vowels_map[word[r]] += 1
                    r += 1
            return ans
        
        return countAtLeastMConsonants(k) - countAtLeastMConsonants(k + 1)

"""
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        def fn(op): 
            ans = []
            vowel = Counter()
            consonant = j = 0 
            for i, ch in enumerate(word): 
                if ch in "aeiou": vowel[ch] += 1
                else: consonant += 1
                while len(vowel) == 5 and op(consonant, k): 
                    if word[j] in "aeiou": 
                        vowel[word[j]] -= 1
                        if vowel[word[j]] == 0: vowel.pop(word[j])
                    else: consonant -= 1
                    j += 1
                ans.append(j)
            return ans
        
        return sum(hi-lo for hi, lo in zip(fn(ge), fn(gt)))
 """               
