class RandomizedSet:

    def __init__(self):
        self.ans = set()
        
    def insert(self, val: int) -> bool:
        if val not in self.ans: 
            self.ans.add(val)
            return True
        return False
        
    def remove(self, val: int) -> bool:
        if val in self.ans:
            self.ans.remove(val)
            return True
        return False
        
    def getRandom(self) -> int:
        x = random.choice(list(self.ans))
        return x
        
