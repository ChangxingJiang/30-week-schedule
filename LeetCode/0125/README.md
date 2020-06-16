# LeetCode题解：0125（验证回文串）

[题目链接](https://leetcode-cn.com/problems/valid-palindrome/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 52ms (>81.43%) |
| Ans 2 (Python) | 64ms (>50.63%) |

解法一（使用Python原生方法）：

```python
def isPalindrome(self, s: str) -> bool:
    s = "".join(filter(str.isalnum, s.lower()))
    return s == s[::-1]
```

解法二（双指针遍历比较）：

```python
def isPalindrome(self, s: str) -> bool:
    index_1 = 0
    index_2 = len(s) - 1
    while index_1 < index_2:
        if not s[index_1].lower().isalnum():
            index_1 += 1
            continue
        if not s[index_2].lower().isalnum():
            index_2 -= 1
            continue
        if s[index_1].lower() == s[index_2].lower():
            index_1 += 1
            index_2 -= 1
        else:
            return False
    return True
```