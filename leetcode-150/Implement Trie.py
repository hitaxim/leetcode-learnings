class Trie:

    def __init__(self):
        self.prefix = set()
        self.dic = set()

    def insert(self, word: str) -> None:
        for i in range(len(word)):
            self.prefix.add(word[:i+1])
        self.dic.add(word)

    def search(self, word: str) -> bool:
        return word in self.dic

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefix


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
