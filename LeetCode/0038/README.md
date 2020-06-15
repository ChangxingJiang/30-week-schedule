# LeetCode题解：0038（外观数列）

[题目链接](https://leetcode-cn.com/problems/count-and-say/)（简单）

| 解法           | 执行用时       |
| -------------- | -------------- |
| Ans 1 (Python) | 36ms (>97.26%) |
| Ans 2 (Python) | 48ms (>59.31%) |
| Ans 3 (Python) | 36ms (>97.26%) |

解法一（循环处理）：

```python
def countAndSay(self, n: int) -> str:

    def count(s):
        new = ""
        last = None
        num = 0
        for c in s:
            if c != last:
                if num > 0:
                    new += str(num) + last
                last = c
                num = 1
            else:
                num += 1
        if num > 0:
            new += str(num) + last
        return new

    s = "1"
    for i in range(1, n):
        s = count(s)
    return s
```

解法二（递归实现）：

```python
def countAndSay(self, n: int) -> str:

    def count(s):
        new = ""
        last = None
        num = 0
        for c in s:
            if c != last:
                if num > 0:
                    new += str(num) + last
                last = c
                num = 1
            else:
                num += 1
        if num > 0:
            new += str(num) + last
        return new

    def get_num(n):
        if n == 1:
            return "1"
        else:
            return count(get_num(n - 1))

    return get_num(n)
```

解法三（枚举法）：

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        count_dict = {1: '1', 2: '11', 3: '21', 4: '1211', 5: '111221', 6: '312211', 7: '13112221', 8: '1113213211', 9: '31131211131221', 10: '13211311123113112211',......}
        return count_dict[n]
```