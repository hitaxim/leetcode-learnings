class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])   
        
    
    def next(self) -> int:
        return self.stack.pop().getInteger()        
        
    
    def hasNext(self) -> bool:
        while self.stack:
            current = self.stack[-1]
            if current.isInteger():
                return True
            self.stack.pop()
            nested_list = current.getList()
            for i in range(len(nested_list) - 1, -1, -1):
                self.stack.append(nested_list[i])

        return False   
      
