# LeetCode题解：0121（买股票的最佳时机）

[题目链接](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 48ms (>72.47%) |
| Ans 2 (Python) | 48ms (>72.47%) |

解法一（转换为纯收益计算）：

```python
def maxProfit(self, prices: List[int]) -> int:
    if len(prices) <= 1:
        return 0

    profits = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]

    if max(profits) <= 0:
        return 0

    maximum = 0
    now = 0
    for i in profits:
        now += i
        if now < i:
            now = i
        if now > maximum:
            maximum = now
    return maximum
```

转换为纯收益后，使用最大子序和（53题）的方法计算

解法二（直接计算收益）：

```python
def maxProfit(self, prices: List[int]) -> int:
    maximum = 0
    now = 0
    for i in range(len(prices) - 1):
        profit = prices[i + 1] - prices[i]
        now += profit
        if now < profit:
            now = profit
        if now > maximum:
            maximum = now
    return maximum
```