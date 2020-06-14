# LeetCode题解：0014（最长公共前缀）

[题目链接](https://leetcode-cn.com/problems/longest-common-prefix/)（简单）

| 解法           | 执行用时       | 内存消耗        |
| -------------- | -------------- | --------------- |
| Ans 1 (Python) | 40ms (>78.57%) | 13.7MB (>6.15%) |
| Ans 2 (Python) | 32ms (>97.34%) | 13.5MB (>6.15%) |

解法一（粗暴比较）：

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    # 处理空列表的情况
    if len(strs) == 0:
        return ""

    # 统计最长的字符串长度
    min_len = min([len(s) for s in strs])

    # 处理只有空字符串的情况
    if min_len == 0:
        return ""

    for i in range(min_len):
        t = strs[0][i]
        for s in strs:
            if s[i] != t:
                return strs[0][0:i]
    return strs[0][0:min_len]
```

解法二（转换组的方向进行比较）：

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    ans = ""
    for s in zip(*strs):
        if len(set(s)) != 1:
            return ans
        else:
            ans += s[0]
    return ans
```