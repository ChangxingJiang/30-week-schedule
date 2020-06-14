# LeetCode题解：0009（回文数）

[题目链接](https://leetcode-cn.com/problems/palindrome-number/)（简单）

| 解法           | 执行用时       | 内存消耗        |
| -------------- | -------------- | --------------- |
| Ans 1 (Python) | 164ms (>5.41%) | 13.8MB (>5.88%) |
| Ans 2 (Python) | 92ms (>50.10%) | 13.6MB (>5.88%) |
| Ans 3 (Python) | 84ms (>71.30%) | 13.5MB (>5.88%) |
| Ans 4 (Python) | 72ms (>94.21%) | 13.6MB (>5.88%) |

解法一（转换为列表反转比较）：

```python
def isPalindrome(self, x: int) -> bool:
    l = [c for c in str(x)]
    r = copy.deepcopy(l)
    r.reverse()
    return l == r
```

解法二（通过数值运算反转比较）：

```python
def isPalindrome(self, x: int) -> bool:
    if x < 0:  # 处理负数的情况
        return False

    original = x  # 原始数值
    ans = 0
    while x > 0:
        ans = ans * 10 + x % 10
        x //= 10

    return original == ans
```

解法三（转换为字符串逐个比较）：

```python
def isPalindrome(self, x: int) -> bool:
    s = str(x)

    a = 0
    b = len(s) - 1
    while a <= b:
        if s[a] != s[b]:
            return False
        a += 1
        b -= 1
    return True
```

解法四（转换为字符串反转比较）：

```python
def isPalindrome(self, x: int) -> bool:
    x = str(x)
    y = x[::-1]
    return x == y
```

参考文献：[字符串倒序](https://blog.csdn.net/mingyuli/article/details/81604795)