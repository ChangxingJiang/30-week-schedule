# LeetCode题解：0020（有效的括号）

[题目链接](https://leetcode-cn.com/problems/valid-parentheses/)（简单）

| 解法           | 执行用时       | 内存消耗        |
| -------------- | -------------- | --------------- |
| Ans 1 (Python) | 36ms (>89.92%) | 13.5MB (>5.22%) |

解法一（使用列表存储当前括号状态）：

```python
def isValid(self, s: str) -> bool:

    sign_dict = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    sign_list = []
    for c in s:
        if c in ["(", "[", "{"]:
            sign_list.append(c)
        else:
            r = sign_dict[c]
            if sign_list and r == sign_list[-1]:
                sign_list.pop()
            else:
                return False

    if sign_list:
        return False
    else:
        return True
```