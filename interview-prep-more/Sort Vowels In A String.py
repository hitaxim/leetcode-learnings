class Solution:
    def sortVowels(self, s: str) -> str:

        vowels = ['A', 'E', 'I','O', 'U', 'a', 'e', 'i', 'o', 'u']

        v = []

        for i in s:
            if i in vowels:
                v.append(i)
        k = Counter(v)
        n = []
        for i in vowels:
            if i in v:
                for _ in range(k[i]):
                    n.append(i)

        lst = [i for i in s]
        for i in range(len(lst)):
            if lst[i] in vowels:
                lst[i] = n.pop(0)

        return ''.join(lst)
        
