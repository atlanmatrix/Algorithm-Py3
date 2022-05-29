class MinStack:

    def __init__(self):
        self.sorted_l = []
        self.l = []

    def push(self, val: int) -> None:
        self.l.append(val)
        self.sorted_l = sorted(self.l)

    def pop(self) -> None:
        self.l.pop()
        self.sorted_l = sorted(self.l)

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.sorted_l[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()