class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans = []
        dictionary.sort()
        sentence = sentence.split()

        for i in sentence: 
            flag = 0
            for x in dictionary: 
                if i.startswith(x):
                    ans.append(x)
                    flag = 1
                    break
            if flag == 0: ans.append(i)
        return " ".join(ans)
