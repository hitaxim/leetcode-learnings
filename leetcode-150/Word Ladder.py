class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        wordq = deque([beginWord])
        distance = 1
        
        while wordq:
            size = len(wordq)
            distance += 1

            for _ in range(size):
                currWord = wordq.popleft()

                for i in range(len(currWord)):
                    for j in range(26):
                        temp = currWord[:i] + chr(ord('a') + j) + currWord[i+1:]

                        if temp == endWord:
                            return distance
                        
                        if temp in wordSet:
                            wordq.append(temp)
                            wordSet.remove(temp)
                
        return  0
