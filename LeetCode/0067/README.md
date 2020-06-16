# LeetCode题解：0067（二进制求和）

[题目链接](https://leetcode-cn.com/problems/add-binary/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 44ms (>65.80%) |
| Ans 2 (Python) | 40ms (>82.92%) |

解法一（转换为二进制数计算）：

```python
def addBinary(self, a: str, b: str) -> str:
    a = int(a, 2)
    b = int(b, 2)
    s = a + b
    s = bin(s)
    return str(s).replace("0b", "")
```

解法二（硬解二进制）：

```python
def addBinary(self, a: str, b: str) -> str:
    a = [int(t) for t in a]
    b = [int(t) for t in b]

    len_a = len(a)
    len_b = len(b)

    s = []
    add = 0
    for i in range(1, max(len_a, len_b) + 1):
        c = add
        if i <= len_a:
            c += a[-i]
        if i <= len_b:
            c += b[-i]
        if c == 0:
            s.insert(0, "0")
            add = 0
        elif c == 1:
            s.insert(0, "1")
            add = 0
        elif c == 2:
            s.insert(0, "0")
            add = 1
        else:
            s.insert(0, "1")
            add = 1
    if add == 1:
        s.insert(0, "1")
    return "".join(s)
```