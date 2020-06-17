# LeetCode题解：0130（只出现一次的数字）

[题目链接](https://leetcode-cn.com/problems/single-number/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 44ms (>78.95%) |
| Ans 2 (Python) | 48ms (>61.14%) |

解法一（使用哈希表实现）：

```python
def singleNumber(self, nums: List[int]) -> int:
    hashset = set()
    for n in nums:
        if n not in hashset:
            hashset.add(n)
        else:
            hashset.remove(n)
    return hashset.pop()
```

解法二（位运算实现）：

```python
def singleNumber(self, nums: List[int]) -> int:
    s = 0
    for n in nums:
        s = s ^ n
    return s
```