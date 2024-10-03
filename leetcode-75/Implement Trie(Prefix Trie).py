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
