# LeetCode题解：0122（买股票的最佳时机II）

[题目链接](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 72ms (>62.45%) |

解法一（直接累加所有可能的收益即可）：

```python
def maxProfit(self, prices: List[int]) -> int:
    sum = 0
    for i in range(len(prices) - 1):
        profit = prices[i + 1] - prices[i]
        if profit > 0:
            sum += profit
    return sum
```