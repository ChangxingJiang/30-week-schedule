# LeetCode题解：0168（Excel表列名称）

[题目链接](https://leetcode-cn.com/problems/excel-sheet-column-title/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 32ms (>94.39%) |

解法一：

```python
def convertToTitle(self, n: int) -> str:
    ans = []
    while n > 0:
        ans.append(chr((n - 1) % 26 + 65))
        n = (n - 1) // 26
    ans.reverse()
    return "".join(ans)
```