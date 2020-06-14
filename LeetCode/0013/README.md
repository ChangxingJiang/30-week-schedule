# LeetCode题解：0013（罗马数字转整数）

[题目链接](https://leetcode-cn.com/problems/roman-to-integer/)（简单）

| 解法           | 执行用时       | 内存消耗        |
| -------------- | -------------- | --------------- |
| Ans 1 (Python) | 52ms (>92.57%) | 13.7MB (>6.45%) |

解法一（观察发现，先直接统计总数；当发现小数出现在大数的左侧时，则减去两次小数）：

```python
def romanToInt(self, s: str) -> int:

    number = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    t = None  # 上一个字符
    ans = 0  # 数值总计
    for c in s:
        if t:
            if number[t] < number[c]:
                ans -= number[t] * 2
            ans += number[c]
        else:
            ans += number[c]
        t = c
    return ans
```



