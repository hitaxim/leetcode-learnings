class TrieNode: 
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        for w in words:
            node = root
            for ch in w: 
                if ch not in node.children: 
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                node.count += 1
        result = []
        for word in words: 
            node = root
            score = 0
            for ch in word:
                node = node.children[ch]
                score += node.count
            result.append(score)
        return result
