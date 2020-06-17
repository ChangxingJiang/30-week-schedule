# LeetCode题解：0172（阶乘后的零）

[题目链接](https://leetcode-cn.com/problems/factorial-trailing-zeroes/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 超出时间限制   |
| Ans 2 (Python) | 36ms (>89.34%) |

解法一（统计每个阶乘数值中因子5的出现次数）：

```python
def trailingZeroes(self, n: int) -> int:
    count = 0
    for i in range(1, n + 1):
        while i % 5 == 0:
            count += 1
            i = i / 5
    return count
```

解法二（直接统计序数5的出现次数）：

```python
def trailingZeroes(self, n: int) -> int:
    count = 0
    now = 5
    while now <= n:
        count += n // now
        now *= 5
    return count
```