class AllOne:
    def __init__(self):
        self.count = defaultdict(int)
        self.freq = defaultdict(set)
    def inc(self, key: str) -> None:
        cnt = self.count[key]
        if cnt > 0:
            self.freq[cnt].remove(key)
        self.count[key] += 1
        self.freq[cnt + 1].add(key)
        if not self.freq[cnt]:
            del self.freq[cnt]
    def dec(self, key: str) -> None:
        cnt = self.count[key]
        self.freq[cnt].remove(key)
        if cnt == 1:
            del self.count[key]
        else:
            self.count[key] -= 1
            self.freq[cnt - 1].add(key)
        if not self.freq[cnt]:
            del self.freq[cnt]
    def getMaxKey(self) -> str:
        return next(iter(self.freq[max(self.freq)]), "") if self.freq else ""
    def getMinKey(self) -> str:
        return next(iter(self.freq[min(self.freq)]), "") if self.freq else ""


"""class AllOne:
    def __init__(self):
        self.myDict = {}

    def inc(self, key: str) -> None:
        if key in self.myDict:
            self.myDict[key] += 1
        else:
            self.myDict[key] = 1

    def dec(self, key: str) -> None:
        if key in self.myDict:
            if self.myDict[key] > 1:
                self.myDict[key] -= 1
            else:
                self.myDict.pop(key)

    def getMaxKey(self) -> str:
        if not self.myDict:
            return ""
        maxVal = max(self.myDict.values())
        for key in self.myDict.keys():
            if self.myDict[key] == maxVal:
                return key

    def getMinKey(self) -> str:
        if not self.myDict:
            return ""
        minVal = min(self.myDict.values())
        for key in self.myDict.keys():
            if self.myDict[key] == minVal:
                return key
"""

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
