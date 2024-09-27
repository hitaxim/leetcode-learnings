class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')

        if len(words) != len(pattern):
            return False

        #if len(set(pattern)) != len(set(words)): 
        #    return False

        list1 = []
        list2 = []
        for i in pattern:
            list1.append(pattern.index(i))
        
        for j in words:
            list2.append(words.index(j))
        #print(list1)

        if list1 == list2:
            return True
        else:
            return False
