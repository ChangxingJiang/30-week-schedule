# LeetCode题解：0171（Excel列表序号）

[题目链接](https://leetcode-cn.com/problems/excel-sheet-column-number/)（简单）

与题目168互为相反。

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 36ms (>93.00%) |

解法一：

```python
def titleToNumber(self, s: str) -> int:
    ans = 0
    for i in range(len(s)):
        ans += (ord(s[-(i + 1)]) - 64) * pow(26, i)
    return ans
```

