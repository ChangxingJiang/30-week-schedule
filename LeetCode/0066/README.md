# LeetCode题解：0066（加一）

[题目链接](https://leetcode-cn.com/problems/plus-one/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 40ms (>68.09%) |

解法一（从后向前遍历进位）：

```python
def plusOne(self, digits: List[int]) -> List[int]:
    for i in range(-1, -len(digits) - 1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    digits.insert(0, 1)
    return digits
```