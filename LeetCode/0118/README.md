# LeetCode题解：0118（杨辉三角）

[题目链接](https://leetcode-cn.com/problems/pascals-triangle/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 40ms (>64.05%) |

解法一（遍历生成）：

```python
def generate(self, numRows: int) -> List[List[int]]:
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]

    ans = [[1]]
    last_line = [1]
    for _ in range(numRows - 1):
        now_line = [1]
        for j in range(len(last_line) - 1):
            now_line.append(last_line[j] + last_line[j + 1])
        now_line.append(1)
        last_line = now_line
        ans.append(now_line)
    return ans
```