# LeetCode题解：0007（整数反转）

[题目链接](https://leetcode-cn.com/problems/reverse-integer/)（简单）

| 解法           | 执行用时       | 内存消耗        |
| -------------- | -------------- | --------------- |
| Ans 1 (Python) | 64ms (>6.66%)  | 13.6MB (>6.67%) |
| Ans 2 (Python) | 40ms (>83.92%) | 13.7MB (>6.67%) |

解法一（转换为字符串反转）：

```python
def reverse(self, x: int) -> int:
    l = [c for c in str(x).replace("-", "")]
    l.reverse()
    ans = int("".join(l))
    if -pow(2, 31) < ans < pow(2, 31) - 1:
        if x >= 0:
            return ans
        else:
            return -ans
    else:
        return 0
```

解法二（通过数值运算反转）：

```python
def reverse(self, x: int) -> int:
    if x < 0:
        x = abs(x)
        pre = -1
    else:
        pre = 1

    ans = 0
    while x > 0:
        num = x % 10
        x = x // 10
        ans = ans * 10 + num

    limit = pow(2, 31)
    if -limit < ans < limit - 1:
        return pre * ans
    else:
        return 0
```

