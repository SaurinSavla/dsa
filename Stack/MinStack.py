class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        tmp = []
        minimum = self.stack[-1]

        while self.stack:
            tmp.append(self.stack[-1])
            minimum = min(minimum, self.stack[-1])
            self.stack.pop()
        while tmp:
            self.stack.append(tmp[-1])
            tmp.pop()
        return minimum

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()