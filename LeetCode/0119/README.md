# LeetCode题解：0119（杨辉三角II）

[题目链接](https://leetcode-cn.com/problems/pascals-triangle-ii/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 32ms (>96.67%) |

解法一（迭代生成）：

```python
def getRow(self, rowIndex: int) -> List[int]:
    if rowIndex == 0:
        return [1]
    else:
        row = [1, 1]
        for _ in range(1, rowIndex):
            new_row = [1]
            for i in range(len(row) - 1):
                new_row.append(row[i] + row[i + 1])
            new_row.append(1)
            row = new_row
        return row
```