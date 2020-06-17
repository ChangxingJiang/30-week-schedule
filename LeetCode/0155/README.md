# LeetCode题解：0155（最小栈）

[题目链接](https://leetcode-cn.com/problems/min-stack/)（简单）

| 解法           | 执行用时        |
| :------------- | --------------- |
| Ans 1 (Python) | 704ms (>20.85%) |
| Ans 2 (Python) | 76ms (>83.93%)  |

解法一（使用Python的list直接实现）：

```python
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
```

解法二（同时存储栈和最小值）：

```python
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
```