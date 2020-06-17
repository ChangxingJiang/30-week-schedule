class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.minimum = None

    def push(self, x: int) -> None:
        self.nums.append(x)
        if self.minimum is None or self.minimum > x:
            self.minimum = x

    def pop(self) -> None:
        x = self.nums.pop(-1)
        if self.minimum == x:
            if len(self.nums) >= 1:
                self.minimum = min(self.nums)
            else:
                self.minimum = None

    def top(self) -> int:
        if len(self.nums) >= 1:
            return self.nums[-1]

    def getMin(self) -> int:
        return self.minimum


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # -3
    minStack.pop()
    print(minStack.top())  # 0
    print(minStack.getMin())  # -2
