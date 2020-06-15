# LeetCode题解：0028（实现strStr()）

[题目链接](https://leetcode-cn.com/problems/implement-strstr/)（简单）

| 解法           | 执行用时       |
| -------------- | -------------- |
| Ans 1 (Python) | 40ms (>78.00%) |
| Ans 2 (Python) | 52ms (>34.29%) |
| Ans 3 (Python) | 44ms (>61.00%) |

解法一（使用Python原生index实现）：

```python
def strStr(self, haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1
```

解法二（逐字符比较；每次查找失败转移到开始坐标的下一个字节）：

```python
def strStr(self, haystack: str, needle: str) -> int:
    needle_len = len(needle)

    # 处理长度为0的情况
    if needle_len == 0:
        return 0

    # 循环处理字符串
    j = 0
    i = 0
    while i < len(haystack):
        c = haystack[i]
        if c == needle[j]:
            if j == needle_len - 1:
                return i - j
            else:
                j += 1
            i += 1
        else:
            i = i - j + 1
            j = 0
    return -1
```

解法三（遍历字符串，查看每个坐标是否为needle的起始坐标）：

```python
def strStr(self, haystack: str, needle: str) -> int:
    len_h = len(haystack)
    len_n = len(needle)
    for i in range(len_h - len_n + 1):
        if haystack[i: i + len_n] == needle:
            return i
    return -1
```