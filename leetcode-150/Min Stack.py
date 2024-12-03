class MinStack:

    def __init__(self):
        self.stack = []
        self.minv = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minv or val <= self.minv[-1]:
            self.minv.append(val)
        
    def pop(self) -> None:
        val = self.stack.pop()
        if self.minv and val == self.minv[-1]:
            self.minv.pop()
        
    def top(self) -> int:
        if self.stack: 
            return self.stack[-1]
        return -1
        
    def getMin(self) -> int:
        if self.minv: 
            return self.minv[-1]
        return -1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
