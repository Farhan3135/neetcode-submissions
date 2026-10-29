class MinStack:

    def __init__(self):
        self.mainStack = []
        self.minStack = []
        
    def push(self, value: int) -> None:
        if not self.mainStack: 
            self.mainStack.append(value)
            self.minStack.append(value)
            return None

        if value <= self.minStack[-1]:
            self.mainStack.append(value)
            self.minStack.append(value)
        else:
            self.mainStack.append(value)
            self.minStack.append(self.minStack[-1])



    def pop(self) -> None:
        self.minStack.pop()
        self.mainStack.pop()
        

    def top(self) -> int:
        return self.mainStack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()