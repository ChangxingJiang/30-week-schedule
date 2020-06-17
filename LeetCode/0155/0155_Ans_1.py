class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.maximum = None
        self.minimum = None

    def push(self, x: int) -> None:
        self.nums.append(x)

    def pop(self) -> None:
        self.nums.pop(-1)

    def top(self) -> int:
        if len(self.nums) >= 1:
            return self.nums[-1]

    def getMin(self) -> int:
        return min(self.nums)


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # -3
    minStack.pop()
    print(minStack.top())  # 0
    print(minStack.getMin())  # -2
